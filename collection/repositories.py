from __future__ import annotations

from typing import Iterable, Sequence

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Case, Count, Exists, FloatField, OuterRef, Prefetch, QuerySet, When
from django.db.models.functions import Cast

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
        search: str | None = None,
        ordering: str | None = None,
    ) -> CollectionListResult:
        queryset = self._base_queryset(subscriber_id=subscriber_id)
        if owner_id is not None:
            queryset = queryset.filter(owner_id=owner_id)
        if is_public is not None:
            queryset = queryset.filter(is_public=is_public)
        if search:
            queryset = queryset.filter(name__icontains=search)
        if subscribed is True and subscriber_id is not None:
            queryset = queryset.filter(subscriptions__user_id=subscriber_id)
        elif subscribed is False and subscriber_id is not None:
            queryset = queryset.exclude(subscriptions__user_id=subscriber_id)

        order_fields = self._resolve_list_ordering(ordering)
        if order_fields:
            queryset = queryset.order_by(*order_fields)

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
                design=payload.design or '',
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
        if payload.design is not None:
            collection.design = payload.design
            update_fields.append('design')
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
        title_search: str | None = None,
        genres: str | None = None,
        year: str | None = None,
        imdb_id: str | None = None,
        rating_min: float | None = None,
        rating_max: float | None = None,
        ordering: str | None = None,
    ) -> CollectionMovieListResult:
        base_qs = CollectionMovie.objects.filter(collection_id=collection_id).select_related('movie')
        needs_rating_value = rating_min is not None or rating_max is not None or self._ordering_needs_rating(ordering)
        if needs_rating_value:
            base_qs = base_qs.annotate(
                imdb_rating_value=Case(
                    When(movie__imdb_rating__regex=r'^\d+(\.\d+)?$', then=Cast('movie__imdb_rating', FloatField())),
                    default=None,
                    output_field=FloatField(),
                )
            )
        if title_search:
            base_qs = base_qs.filter(movie__title__icontains=title_search)
        if genres:
            base_qs = base_qs.filter(movie__genres__name__icontains=genres)
        if year:
            base_qs = base_qs.filter(movie__year__icontains=year)
        if imdb_id:
            base_qs = base_qs.filter(movie__imdb_id__exact=imdb_id)
        if rating_min is not None:
            base_qs = base_qs.filter(imdb_rating_value__gte=rating_min)
        if rating_max is not None:
            base_qs = base_qs.filter(imdb_rating_value__lte=rating_max)

        order_fields = self._resolve_ordering(ordering)
        base_qs = base_qs.order_by(*order_fields).distinct()
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
                description=relation.movie.plot,
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
            design=source.design,
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
            .annotate(movies_count=Count('collection_movies', distinct=True), subscribers_count=Count('subscriptions', distinct=True))
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

    def _resolve_list_ordering(self, ordering: str | None) -> list[str] | None:
        if not ordering:
            return None

        allowed_fields = {
            'created_at': ['created_at', 'id'],
            'subscribers': ['subscribers_count', 'id'],
        }
        parts = [part.strip() for part in ordering.split(',') if part.strip()]
        if not parts:
            return None

        order_fields: list[str] = []
        for part in parts:
            descending = part.startswith('-')
            field_key = part[1:] if descending else part
            if field_key not in allowed_fields:
                raise ValidationError({'ordering': f'Unsupported ordering: {part}'})
            for field in allowed_fields[field_key]:
                order_fields.append(f'-{field}' if descending else field)
        return order_fields

    def _resolve_ordering(self, ordering: str | None) -> list[str]:
        if not ordering:
            return ['position', 'added_at', 'id']

        allowed_fields = {
            'position': ['position', 'id'],
            'added_at': ['added_at', 'id'],
            'title': ['movie__title', 'id'],
            'year': ['movie__year', 'id'],
            'imdb_id': ['movie__imdb_id', 'id'],
            'imdb_rating': ['imdb_rating_value', 'id'],
        }
        parts = [part.strip() for part in ordering.split(',') if part.strip()]
        if not parts:
            return ['position', 'added_at', 'id']

        order_fields: list[str] = []
        for part in parts:
            descending = part.startswith('-')
            field_key = part[1:] if descending else part
            if field_key not in allowed_fields:
                raise ValidationError({'ordering': f'Unsupported ordering: {part}'})
            for field in allowed_fields[field_key]:
                order_fields.append(f'-{field}' if descending else field)

        return order_fields

    @staticmethod
    def _ordering_needs_rating(ordering: str | None) -> bool:
        if not ordering:
            return False
        return any(segment.strip().lstrip('-') == 'imdb_rating' for segment in ordering.split(','))

    @staticmethod
    def _to_dto(collection: Collection) -> CollectionDTO:
        return CollectionDTO(
            id=collection.id,
            name=collection.name,
            description=collection.description,
            design=collection.design,
            is_public=collection.is_public,
            owner_id=collection.owner_id,
            owner_email=getattr(collection.owner, 'email', None),
            movies_count=getattr(collection, 'movies_count', 0),
            is_subscribed=getattr(collection, 'is_subscribed', False),
            subscribers_count=getattr(collection, 'subscribers_count', 0),
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
