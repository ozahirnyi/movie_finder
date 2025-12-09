from django.core.exceptions import ValidationError as DjangoValidationError
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from movie.paginations import MoviesPagination

from .serializers import (
    CollectionCreateSerializer,
    CollectionMovieSerializer,
    CollectionSerializer,
    CollectionUpdateSerializer,
    EmptySerializer,
)
from .services import CollectionService


class CollectionListCreateView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CollectionSerializer
    pagination_class = MoviesPagination
    service_class = CollectionService

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='limit',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Number of collections to return (default 12).',
                required=False,
            ),
            OpenApiParameter(
                name='offset',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Pagination offset.',
                required=False,
            ),
            OpenApiParameter(
                name='is_public',
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description='Filter collections by visibility.',
                required=False,
            ),
            OpenApiParameter(
                name='owner_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Filter collections by owner id (restricted to requester visibility rules).',
                required=False,
            ),
            OpenApiParameter(
                name='subscribed',
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description='When true, return only collections the requester is subscribed to; when false, return only unsubscribed ones.',
                required=False,
            ),
        ],
        responses=CollectionSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        service = self.service_class()
        is_public = self._get_bool_query_param(request.query_params.get('is_public'))
        subscribed = self._get_bool_query_param(request.query_params.get('subscribed'))
        owner_id = request.query_params.get('owner_id')
        owner_id_int = self._parse_owner_id(owner_id)
        pagination = self.pagination_class() if self.pagination_class else None
        limit = offset = None
        if pagination:
            pagination.request = request
            limit = pagination.get_limit(request)
            offset = pagination.get_offset(request)
        result = service.list_collections(
            viewer_id=request.user.id,
            is_staff=bool(getattr(request.user, 'is_staff', False)),
            is_public=is_public,
            owner_id=owner_id_int,
            subscribed=subscribed,
            limit=limit,
            offset=offset,
        )
        serializer = CollectionSerializer(result.items, many=True)
        if pagination:
            pagination.count = result.total_count
            pagination.limit = limit
            pagination.offset = offset or 0
            return pagination.get_paginated_response(serializer.data)
        return Response(serializer.data)

    @extend_schema(request=CollectionCreateSerializer, responses=CollectionSerializer)
    def post(self, request, *args, **kwargs):
        serializer = CollectionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = self.service_class()
        collection = service.create_collection(
            owner_id=request.user.id,
            name=serializer.validated_data['name'],
            description=serializer.validated_data.get('description', ''),
            design=serializer.validated_data.get('design', ''),
            is_public=serializer.validated_data.get('is_public', False),
            movie_ids=serializer.validated_data.get('movie_ids'),
        )
        output_serializer = CollectionSerializer(collection)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def _get_bool_query_param(value: str | None) -> bool | None:
        if value is None:
            return None
        if value.lower() in {'true', '1', 'yes'}:
            return True
        if value.lower() in {'false', '0', 'no'}:
            return False
        return None

    @staticmethod
    def _parse_owner_id(value: str | None) -> int | None:
        if value is None:
            return None
        try:
            return int(value)
        except (TypeError, ValueError) as exc:
            raise ValidationError({'owner_id': 'owner_id must be an integer'}) from exc


class CollectionDetailView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CollectionSerializer
    service_class = CollectionService
    lookup_url_kwarg = 'collection_id'

    def get(self, request, *args, **kwargs):
        collection = self._safe_get_collection()
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    @extend_schema(request=CollectionUpdateSerializer, responses=CollectionSerializer)
    def patch(self, request, *args, **kwargs):
        serializer = CollectionUpdateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        service = self.service_class()
        try:
            collection = service.update_collection(
                viewer_id=request.user.id,
                is_staff=bool(getattr(request.user, 'is_staff', False)),
                collection_id=self._get_collection_id(),
                name=serializer.validated_data.get('name'),
                description=serializer.validated_data.get('description'),
                design=serializer.validated_data.get('design'),
                is_public=serializer.validated_data.get('is_public'),
                movie_ids=serializer.validated_data.get('movie_ids') if 'movie_ids' in serializer.validated_data else None,
            )
        except PermissionError as exc:
            raise PermissionDenied(str(exc)) from exc
        output_serializer = CollectionSerializer(collection)
        return Response(output_serializer.data)

    def delete(self, request, *args, **kwargs):
        service = self.service_class()
        try:
            service.delete_collection(
                viewer_id=request.user.id,
                is_staff=bool(getattr(request.user, 'is_staff', False)),
                collection_id=self._get_collection_id(),
            )
        except PermissionError as exc:
            raise PermissionDenied(str(exc)) from exc
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _safe_get_collection(self):
        service = self.service_class()
        try:
            return service.retrieve_collection(
                viewer_id=self.request.user.id,
                is_staff=bool(getattr(self.request.user, 'is_staff', False)),
                collection_id=self._get_collection_id(),
            )
        except PermissionError as exc:
            raise PermissionDenied(str(exc)) from exc

    def _get_collection_id(self) -> int:
        return int(self.kwargs[self.lookup_url_kwarg])


class CollectionMoviesView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CollectionMovieSerializer
    pagination_class = MoviesPagination
    service_class = CollectionService
    lookup_url_kwarg = 'collection_id'

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='search',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter collection movies by title (case-insensitive).',
                required=False,
            ),
            OpenApiParameter(
                name='genres',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter collection movies by genre name (case-insensitive).',
                required=False,
            ),
            OpenApiParameter(
                name='year',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter collection movies by year.',
                required=False,
            ),
            OpenApiParameter(
                name='imdb_id',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter collection movies by exact IMDb id.',
                required=False,
            ),
            OpenApiParameter(
                name='rating_min',
                type=OpenApiTypes.FLOAT,
                location=OpenApiParameter.QUERY,
                description='Return movies with IMDb rating greater than or equal to this value.',
                required=False,
            ),
            OpenApiParameter(
                name='rating_max',
                type=OpenApiTypes.FLOAT,
                location=OpenApiParameter.QUERY,
                description='Return movies with IMDb rating less than or equal to this value.',
                required=False,
            ),
            OpenApiParameter(
                name='ordering',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Order collection movies by allowed fields: position, added_at, title, '
                'year, imdb_id, imdb_rating (prefix with - for descending).',
                required=False,
            ),
        ],
        responses=CollectionMovieSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        service = self.service_class()
        pagination = self.pagination_class() if self.pagination_class else None
        limit = offset = None
        if pagination:
            pagination.request = request
            limit = pagination.get_limit(request)
            offset = pagination.get_offset(request)
        try:
            result = service.list_collection_movies(
                viewer_id=request.user.id,
                is_staff=bool(getattr(request.user, 'is_staff', False)),
                collection_id=self._get_collection_id(),
                limit=limit,
                offset=offset,
                title_search=request.query_params.get('search'),
                genres=request.query_params.get('genres'),
                year=request.query_params.get('year'),
                imdb_id=request.query_params.get('imdb_id'),
                rating_min=self._parse_float(request.query_params.get('rating_min'), 'rating_min'),
                rating_max=self._parse_float(request.query_params.get('rating_max'), 'rating_max'),
                ordering=request.query_params.get('ordering'),
            )
        except PermissionError as exc:
            raise PermissionDenied(str(exc)) from exc
        except DjangoValidationError as exc:
            raise ValidationError(exc.message_dict) from exc
        movie_serializer = CollectionMovieSerializer(result.items, many=True)
        if pagination:
            pagination.count = result.total_count
            pagination.limit = limit
            pagination.offset = offset or 0
            return pagination.get_paginated_response(movie_serializer.data)
        return Response(movie_serializer.data)

    def _get_collection_id(self) -> int:
        return int(self.kwargs[self.lookup_url_kwarg])

    @staticmethod
    def _parse_float(value: str | None, field_name: str) -> float | None:
        if value is None:
            return None
        try:
            return float(value)
        except (TypeError, ValueError) as exc:
            raise ValidationError({field_name: f'{field_name} must be a number'}) from exc


class CollectionSubscriptionView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmptySerializer
    service_class = CollectionService
    lookup_url_kwarg = 'collection_id'

    @extend_schema(request=None, responses={204: None})
    def post(self, request, *args, **kwargs):
        service = self.service_class()
        try:
            service.subscribe(
                viewer_id=request.user.id,
                is_staff=bool(getattr(request.user, 'is_staff', False)),
                collection_id=self._get_collection_id(),
            )
        except PermissionError as exc:
            raise PermissionDenied(str(exc)) from exc
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(request=None, responses={204: None})
    def delete(self, request, *args, **kwargs):
        service = self.service_class()
        service.unsubscribe(viewer_id=request.user.id, collection_id=self._get_collection_id())
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_collection_id(self) -> int:
        return int(self.kwargs[self.lookup_url_kwarg])


class CollectionCloneView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CollectionSerializer
    service_class = CollectionService
    lookup_url_kwarg = 'collection_id'

    def post(self, request, *args, **kwargs):
        service = self.service_class()
        try:
            cloned = service.clone_collection(
                viewer_id=request.user.id,
                is_staff=bool(getattr(request.user, 'is_staff', False)),
                collection_id=self._get_collection_id(),
            )
        except PermissionError as exc:
            raise PermissionDenied(str(exc)) from exc
        except DjangoValidationError as exc:
            raise ValidationError(exc.message_dict) from exc
        output_serializer = CollectionSerializer(cloned)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    def _get_collection_id(self) -> int:
        return int(self.kwargs[self.lookup_url_kwarg])
