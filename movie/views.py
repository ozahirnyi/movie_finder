from django.db import IntegrityError
from django.db.models import Case, Count, Value, When
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from throttling.throttling import (
    RegularSearchForwardedThrottle,
    RegularSearchIpThrottle,
    RegularSearchUaThrottle,
)

from .errors import AddLikeError
from .filters import MovieFilter, WatchLaterFilter
from .models import LikeMovie, Movie, WatchLaterMovie
from .paginations import MoviesPagination
from .serializers import (
    FindMovieAiSearchViewRequestSerializer,
    FindMovieSearchViewRequestSerializer,
    MovieModelSerializer,
    MovieSerializer,
    WatchLaterCreateSerializer,
    WatchLaterListSerializer,
    WatchLaterStatisticsGenreSerializer,
    WatchLaterStatisticsRatingSerializer,
    WatchLaterStatisticsSerializer,
)
from .services import MovieService


class MovieView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieModelSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Movie.objects.with_is_liked(self.request.user.id).with_is_watch_later(self.request.user.id).with_likes_count().with_watch_later_count()


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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='ordering',
            description='Comma-separated list of ordering fields. Prefix with `-` for descending order.',
            required=False,
            type=str,
            enum=['-imdb_id', 'imdb_id', '-title', 'title', '-genre', 'genre', '-year', 'year', '-likes_count', 'likes_count'],
        ),
    ]
)
class MoviesListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieModelSerializer
    pagination_class = MoviesPagination
    throttle_classes = [
        RegularSearchUaThrottle,
        RegularSearchIpThrottle,
        RegularSearchForwardedThrottle,
    ]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['title']
    ordering_fields = ['imdb_id', 'title', 'genre', 'year', 'likes_count']
    ordering = ['imdb_id']

    def get_queryset(self):
        return (
            Movie.objects.all()
            .with_is_liked(self.request.user.id)
            .with_is_watch_later(self.request.user.id)
            .with_likes_count()
            .with_watch_later_count()
        )


class MoviesSearchView(APIView):
    permission_classes = [permissions.AllowAny]
    throttle_classes = [
        RegularSearchUaThrottle,
        RegularSearchIpThrottle,
        RegularSearchForwardedThrottle,
    ]

    @extend_schema(
        request=FindMovieSearchViewRequestSerializer,
        responses={status.HTTP_200_OK: MovieSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        input_serializer = FindMovieSearchViewRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        movie_service = MovieService()
        imdb_movies = movie_service.get_movies_from_imdb(input_serializer.data.get('expression'))
        omdb_movies = movie_service.search_movies_in_omdb([movie.title for movie in imdb_movies], self.request.user.id)
        serialized_movies = MovieSerializer(omdb_movies, many=True)
        return Response(serialized_movies.data, status=status.HTTP_200_OK)


class MoviesAiSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # throttle_classes = [
    #     AiSearchUaThrottle,
    #     AiSearchIpThrottle,
    #     AiSearchForwardedThrottle,
    # ]

    @extend_schema(
        request=FindMovieAiSearchViewRequestSerializer,
        responses={status.HTTP_200_OK: MovieSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        input_serializer = FindMovieAiSearchViewRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        movie_service = MovieService()
        ai_movies = movie_service.get_movies_from_ai(input_serializer.data.get('expression'))
        omdb_movies = movie_service.search_movies_in_omdb([movie.title for movie in ai_movies], self.request.user.id)
        serialized_movies = MovieSerializer(omdb_movies, many=True)
        return Response(serialized_movies.data, status=status.HTTP_200_OK)


class WatchLaterCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='ordering',
            description='Comma-separated list of ordering fields. Prefix with `-` for descending order.',
            required=False,
            type=str,
            enum=['-imdb_id', 'imdb_id', '-title', 'title', '-genre', 'genre', '-year', 'year', '-likes_count', 'likes_count'],
        ),
    ]
)
class WatchLaterListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterListSerializer
    pagination_class = MoviesPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = WatchLaterFilter
    search_fields = ['title']
    ordering_fields = ['imdb_id', 'title', 'genre', 'year']
    ordering = ['imdb_id']

    def get_queryset(self):
        return (
            Movie.objects.filter(watchlatermovie__user_id=self.request.user.id)
            .with_is_liked(self.request.user.id)
            .with_is_watch_later(self.request.user.id)
            .with_likes_count()
            .with_watch_later_count()
        )


class WatchLaterStatisticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        rating_stats = WatchLaterMovie.objects.filter(user=self.request.user).aggregate(
            ratings_9_plus=Count(Case(When(movie__movie_ratings__value__gte='9.0', then=Value(1)))),
            ratings_8_to_9=Count(Case(When(movie__movie_ratings__value__gte='8.0', movie__movie_ratings__value__lt='9.0', then=Value(1)))),
            ratings_7_to_8=Count(Case(When(movie__movie_ratings__value__gte='7.0', movie__movie_ratings__value__lt='8.0', then=Value(1)))),
            ratings_6_to_7=Count(Case(When(movie__movie_ratings__value__gte='6.0', movie__movie_ratings__value__lt='7.0', then=Value(1)))),
            ratings_5_to_6=Count(Case(When(movie__movie_ratings__value__gte='5.0', movie__movie_ratings__value__lt='6.0', then=Value(1)))),
            ratings_below_5=Count(Case(When(movie__movie_ratings__value__lt='5.0', then=Value(1)))),
        )
        ratings_serializer = WatchLaterStatisticsRatingSerializer(data=rating_stats)
        ratings_serializer.is_valid(raise_exception=True)
        genres_stats = (
            WatchLaterMovie.objects.filter(user=self.request.user)
            .values('movie__genres__name')
            .annotate(count=Count('movie__genres'))
            .order_by('-count')
        )
        genres_data = [{'genre': g['movie__genres__name'], 'count': g['count']} for g in genres_stats]
        genres_serializer = WatchLaterStatisticsGenreSerializer(data=genres_data, many=True)
        genres_serializer.is_valid(raise_exception=True)
        serializer = WatchLaterStatisticsSerializer(
            data={
                'ratings': ratings_serializer.validated_data,
                'genres': genres_serializer.validated_data,
            }
        )
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)


class WatchLaterDestroyView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        WatchLaterMovie.objects.filter(user_id=self.request.user.id, movie_id=kwargs.get('pk')).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
