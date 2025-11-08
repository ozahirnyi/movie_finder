from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from movie.paginations import MoviesPagination

from .serializers import (
    CollectionCreateSerializer,
    CollectionSerializer,
    CollectionUpdateSerializer,
)
from .services import CollectionService


class CollectionListCreateView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
        ],
        responses=CollectionSerializer(many=True),
    )
    def get(self, request, *args, **kwargs):
        service = self.service_class()
        is_public = self._get_bool_query_param(request.query_params.get('is_public'))
        owner_id = request.query_params.get('owner_id')
        owner_id_int = self._parse_owner_id(owner_id)
        pagination = self.pagination_class() if self.pagination_class else None
        limit = offset = None
        if pagination:
            pagination.request = request
            limit = pagination.get_limit(request)
            offset = pagination.get_offset(request)
        result = service.list_collections(
            user=request.user,
            is_public=is_public,
            owner_id=owner_id_int,
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
            owner=request.user,
            name=serializer.validated_data['name'],
            description=serializer.validated_data.get('description', ''),
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
                user=request.user,
                collection_id=self._get_collection_id(),
                name=serializer.validated_data.get('name'),
                description=serializer.validated_data.get('description'),
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
            service.delete_collection(user=request.user, collection_id=self._get_collection_id())
        except PermissionError as exc:
            raise PermissionDenied(str(exc)) from exc
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _safe_get_collection(self):
        service = self.service_class()
        try:
            return service.retrieve_collection(user=self.request.user, collection_id=self._get_collection_id())
        except PermissionError as exc:
            raise PermissionDenied(str(exc)) from exc

    def _get_collection_id(self) -> int:
        return int(self.kwargs[self.lookup_url_kwarg])
