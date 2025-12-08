from __future__ import annotations

from typing import Iterable, Sequence

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Count, Exists, OuterRef, Prefetch, QuerySet

from movie.models import Movie

from .dataclasses import (
    CollectionDTO,
    CollectionListResult,
    CollectionMovieDTO,
    CollectionMovieListResult,
    CollectionMoviePreviewDTO,
    CollectionPayload,
    CollectionUpdatePayload,
)
from .models import Collection, CollectionMovie, CollectionSubscription


class CollectionRepository:
    def list(
        self,
        *,
        owner_id: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
        is_public: bool | None = None,
        subscriber_id: int | None = None,
        subscribed: bool | None = None,
    ) -> CollectionListResult:
        queryset = self._base_queryset(subscriber_id=subscriber_id)
        if owner_id is not None:
            queryset = queryset.filter(owner_id=owner_id)
        if is_public is not None:
            queryset = queryset.filter(is_public=is_public)
        if subscribed is True and subscriber_id is not None:
            queryset = queryset.filter(subscriptions__user_id=subscriber_id)
        elif subscribed is False and subscriber_id is not None:
            queryset = queryset.exclude(subscriptions__user_id=subscriber_id)

        total_count = queryset.count()
        if offset:
            queryset = queryset[offset:]
        if limit is not None:
            queryset = queryset[:limit]

        collections = list(queryset)
        return CollectionListResult(items=self._to_dtos(collections), total_count=total_count)

    def retrieve(self, collection_id: int, *, viewer_id: int | None = None) -> CollectionDTO:
        collection = self._base_queryset(subscriber_id=viewer_id).get(pk=collection_id)
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
            return self.retrieve(collection.id, viewer_id=payload.owner_id)

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

        return self.retrieve(collection.id, viewer_id=collection.owner_id)

    def delete(self, collection_id: int) -> None:
        Collection.objects.filter(pk=collection_id).delete()

    def list_movies(
        self,
        *,
        collection_id: int,
        limit: int | None = None,
        offset: int | None = None,
    ) -> CollectionMovieListResult:
        base_qs = CollectionMovie.objects.filter(collection_id=collection_id).select_related('movie').order_by('position', 'added_at', 'id')
        total_count = base_qs.count()
        if offset:
            base_qs = base_qs[offset:]
        if limit is not None:
            base_qs = base_qs[:limit]
        items = [
            CollectionMovieDTO(
                id=relation.movie_id,
                title=relation.movie.title,
                imdb_id=relation.movie.imdb_id,
                poster=relation.movie.poster,
                year=relation.movie.year,
            )
            for relation in base_qs
        ]
        return CollectionMovieListResult(items=items, total_count=total_count)

    def subscribe(self, *, collection_id: int, user_id: int) -> None:
        CollectionSubscription.objects.get_or_create(collection_id=collection_id, user_id=user_id)

    def unsubscribe(self, *, collection_id: int, user_id: int) -> None:
        CollectionSubscription.objects.filter(collection_id=collection_id, user_id=user_id).delete()

    def clone(self, *, source_id: int, owner_id: int) -> CollectionDTO:
        source = Collection.objects.get(pk=source_id)
        movie_ids = list(
            CollectionMovie.objects.filter(collection_id=source_id).order_by('position', 'added_at', 'id').values_list('movie_id', flat=True)
        )
        payload = CollectionPayload(
            owner_id=owner_id,
            name=source.name,
            description=source.description,
            is_public=source.is_public,
            movie_ids=movie_ids,
        )
        return self.create(payload)

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

    def _base_queryset(self, *, subscriber_id: int | None = None) -> QuerySet[Collection]:
        queryset = (
            Collection.objects.all()
            .select_related('owner')
            .annotate(movies_count=Count('collection_movies'))
            .prefetch_related(
                Prefetch(
                    'collection_movies',
                    queryset=CollectionMovie.objects.select_related('movie').order_by('position', 'added_at', 'id'),
                    to_attr='prefetched_collection_movies',
                )
            )
        )
        if subscriber_id is not None:
            queryset = queryset.annotate(
                is_subscribed=Exists(CollectionSubscription.objects.filter(collection_id=OuterRef('pk'), user_id=subscriber_id))
            )
        return queryset

    def _to_dtos(self, collections: Sequence[Collection]) -> list[CollectionDTO]:
        return [self._to_dto(collection) for collection in collections]

    @staticmethod
    def _to_dto(collection: Collection) -> CollectionDTO:
        return CollectionDTO(
            id=collection.id,
            name=collection.name,
            description=collection.description,
            is_public=collection.is_public,
            owner_id=collection.owner_id,
            owner_email=getattr(collection.owner, 'email', None),
            movies_count=getattr(collection, 'movies_count', 0),
            is_subscribed=getattr(collection, 'is_subscribed', False),
            preview_movies=CollectionRepository._build_preview_movies(collection),
            created_at=collection.created_at,
            updated_at=collection.updated_at,
        )

    @staticmethod
    def _build_preview_movies(collection: Collection) -> list[CollectionMoviePreviewDTO]:
        prefetched = getattr(collection, 'prefetched_collection_movies', None)
        if prefetched is None:
            relations = list(
                CollectionMovie.objects.filter(collection_id=collection.id, movie__poster__isnull=False)
                .exclude(movie__poster='')
                .select_related('movie')
                .order_by('position', 'added_at', 'id')[:3]
            )
        else:
            relations = prefetched

        preview_movies: list[CollectionMoviePreviewDTO] = []
        for relation in relations:
            movie = getattr(relation, 'movie', None)
            if movie is None or not movie.poster:
                continue
            preview_movies.append(
                CollectionMoviePreviewDTO(
                    id=movie.id,
                    title=movie.title,
                    poster=movie.poster or None,
                )
            )
            if len(preview_movies) == 3:
                break
        return preview_movies
