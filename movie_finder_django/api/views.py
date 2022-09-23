from django.db import IntegrityError, transaction
from django.db.models import Count, OuterRef, Exists
from django.db.transaction import TransactionManagementError
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, DestroyAPIView, CreateAPIView, ListAPIView, get_object_or_404, \
    RetrieveAPIView
from rest_framework.response import Response

from .errors import FindMovieNotExist, AddLikeError
from .models import Movie, WatchLaterMovie, LikeMovie
from .paginations import MoviesPagination
from .serializers import MovieSerializer, WatchLaterCreateSerializer, WatchLaterListSerializer


class MovieView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = Movie.objects.all().annotate(likes_count=Count('likemovie'))

        if self.request.user.is_authenticated:
            qs = qs.annotate(
                is_liked=Exists(LikeMovie.objects.filter(user_id=self.request.user.id, movie_id=OuterRef('pk'))),
            )

        return qs


# class MovieLikeView(CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def post(self, request, *args, **kwargs):
#         user = self.request.user
#         movie_id = kwargs.get('id')
#         like_count = LikeMovie.objects.filter(user=user, movie_id=movie_id).count()
#
#         if like_count == 0:
#             LikeMovie.objects.create(user=user, movie_id=movie_id)
#             return Response(status=status.HTTP_201_CREATED)
#
#         raise AddLikeError


class MovieLikeView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            LikeMovie.objects.create(user=self.request.user, movie_id=kwargs.get('id'))
        except IntegrityError:
            raise AddLikeError

        return Response(status=status.HTTP_201_CREATED)


class MovieUnlikeView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = LikeMovie.objects.all()

    def post(self, request, *args, **kwargs):
        LikeMovie.objects.filter(user=self.request.user, movie_id=kwargs.get('id')).delete()

        return Response(status=status.HTTP_200_OK)


class FindMovieView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    pagination_class = MoviesPagination

    def get(self, *args, **kwargs):
        expression = kwargs.get('expression')

        movie_ids = Movie.get_movies_from_imdb(expression)
        if not len(movie_ids):
            raise FindMovieNotExist
        qs = Movie.objects.filter(pk__in=movie_ids).annotate(likes_count=Count('likemovie'))

        if self.request.user.is_authenticated:
            qs = qs.annotate(
                is_liked=Exists(LikeMovie.objects.filter(user_id=self.request.user.id, movie_id=OuterRef('pk'))),
            )

        qs = self.paginate_queryset(qs)

        data = self.get_serializer(qs, many=True).data
        return self.get_paginated_response(data)


class WatchLaterCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class WatchLaterListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterListSerializer
    pagination_class = MoviesPagination

    def get_queryset(self):
        queryset = WatchLaterMovie.objects.filter(user_id=self.request.user).select_related('movie')

        queryset = self.paginate_queryset(queryset)
        return queryset


class WatchLaterDestroyView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WatchLaterMovie.objects.all()
