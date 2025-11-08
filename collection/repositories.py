from __future__ import annotations

from typing import Iterable, Sequence

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Prefetch, QuerySet

from movie.models import Movie

from .dataclasses import (
    CollectionDTO,
    CollectionListResult,
    CollectionMovieDTO,
    CollectionPayload,
    CollectionUpdatePayload,
)
from .models import Collection, CollectionMovie


class CollectionRepository:
    def list(
        self,
        *,
        owner_id: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
        is_public: bool | None = None,
    ) -> CollectionListResult:
        queryset = self._base_queryset()
        if owner_id is not None:
            queryset = queryset.filter(owner_id=owner_id)
        if is_public is not None:
            queryset = queryset.filter(is_public=is_public)

        total_count = queryset.count()
        if offset:
            queryset = queryset[offset:]
        if limit is not None:
            queryset = queryset[:limit]

        collections = list(queryset)
        return CollectionListResult(items=self._to_dtos(collections), total_count=total_count)

    def retrieve(self, collection_id: int) -> CollectionDTO:
        collection = self._base_queryset().get(pk=collection_id)
        return self._to_dto(collection)

    def create(self, payload: CollectionPayload) -> CollectionDTO:
        with transaction.atomic():
            collection = Collection.objects.create(
                owner_id=payload.owner_id,
                name=payload.name,
                description=payload.description or '',
                is_public=payload.is_public,
            )
            if payload.movie_ids is not None:
                self._replace_movies(collection, payload.movie_ids)
            return self.retrieve(collection.id)

    def update(self, collection_id: int, payload: CollectionUpdatePayload) -> CollectionDTO:
        collection = Collection.objects.get(pk=collection_id)
        update_fields = []
        if payload.name is not None:
            collection.name = payload.name
            update_fields.append('name')
        if payload.description is not None:
            collection.description = payload.description
            update_fields.append('description')
        if payload.is_public is not None:
            collection.is_public = payload.is_public
            update_fields.append('is_public')

        if update_fields:
            collection.save(update_fields=update_fields)

        if payload.movie_ids is not None:
            self._replace_movies(collection, payload.movie_ids)

        return self.retrieve(collection.id)

    def delete(self, collection_id: int) -> None:
        Collection.objects.filter(pk=collection_id).delete()

    def _replace_movies(self, collection: Collection, movie_ids: Iterable[int]) -> None:
        deduped_ids = list(dict.fromkeys(movie_ids))
        movie_map = self._get_movie_map(deduped_ids)
        CollectionMovie.objects.filter(collection=collection).delete()

        entries = [
            CollectionMovie(
                collection=collection,
                movie=movie_map[movie_id],
                position=index,
            )
            for index, movie_id in enumerate(deduped_ids)
        ]
        if entries:
            CollectionMovie.objects.bulk_create(entries)

    def _get_movie_map(self, movie_ids: list[int]) -> dict[int, Movie]:
        if not movie_ids:
            return {}

        movies = Movie.objects.filter(id__in=set(movie_ids))
        movie_map = {movie.id: movie for movie in movies}
        missing_ids = [movie_id for movie_id in movie_ids if movie_id not in movie_map]
        if missing_ids:
            raise ValidationError({'movie_ids': f'Movies not found: {missing_ids}'})
        return movie_map

    def _base_queryset(self) -> QuerySet[Collection]:
        return (
            Collection.objects.all()
            .select_related('owner')
            .prefetch_related(
                Prefetch(
                    'collection_movies',
                    queryset=CollectionMovie.objects.select_related('movie').order_by('position', 'added_at', 'id'),
                )
            )
        )

    def _to_dtos(self, collections: Sequence[Collection]) -> list[CollectionDTO]:
        return [self._to_dto(collection) for collection in collections]

    @staticmethod
    def _to_dto(collection: Collection) -> CollectionDTO:
        movies = [
            CollectionMovieDTO(
                id=relation.movie_id,
                title=relation.movie.title,
                imdb_id=relation.movie.imdb_id,
                poster=relation.movie.poster,
                year=relation.movie.year,
            )
            for relation in collection.collection_movies.all()
        ]
        return CollectionDTO(
            id=collection.id,
            name=collection.name,
            description=collection.description,
            is_public=collection.is_public,
            owner_id=collection.owner_id,
            owner_email=getattr(collection.owner, 'email', None),
            movies=movies,
            created_at=collection.created_at,
            updated_at=collection.updated_at,
        )
