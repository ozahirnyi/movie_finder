from dataclasses import asdict

from django.db import IntegrityError
from django.db.models import Count, OuterRef, Exists
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.generics import (
    GenericAPIView,
    DestroyAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from throttling.throttling import RegularSearchUaThrottle, RegularSearchIpThrottle, RegularSearchForwardedThrottle, \
    AiSearchUaThrottle, AiSearchIpThrottle, AiSearchForwardedThrottle
from .ai_find_movie import FindMovieAiClient
from .errors import AddLikeError
from .models import Movie, WatchLaterMovie, LikeMovie
from .paginations import MoviesPagination
from .serializers import (
    MovieSerializer,
    WatchLaterCreateSerializer,
    WatchLaterListSerializer,
    FindMovieAiViewRequestSerializer
)
from .services import MovieService
from .filters import MovieFilter, WatchLaterFilter
from rest_framework.filters import OrderingFilter


class MovieView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    lookup_field = "id"

    def get_queryset(self):
        return (
            Movie.objects
            .with_is_liked(self.request.user.id)
            .with_is_watch_later(self.request.user.id)
            .with_likes_count()
            .with_watch_later_count()
        )


class MovieLikeView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            LikeMovie.objects.create(user=self.request.user, movie_id=kwargs.get("id"))
        except IntegrityError:
            raise AddLikeError

        return Response(status=status.HTTP_201_CREATED)


class MovieUnlikeView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = LikeMovie.objects.all()

    def post(self, request, *args, **kwargs):
        LikeMovie.objects.filter(
            user=self.request.user, movie_id=kwargs.get("id")
        ).delete()

        return Response(status=status.HTTP_200_OK)


class FindMovieView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    pagination_class = MoviesPagination
    throttle_classes = [RegularSearchUaThrottle, RegularSearchIpThrottle, RegularSearchForwardedThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    search_fields = ['title']
    ordering_fields = ['title', 'genre', 'year']
    ordering = ['title']

    def get_queryset(self):
        queryset = Movie.objects.all()
        expression = self.kwargs.get("expression")
        if expression:
            queryset = queryset.filter(title__icontains=expression)
        return (
            queryset
            .with_is_liked(self.request.user.id)
            .with_is_watch_later(self.request.user.id)
            .with_likes_count()
            .with_watch_later_count()
        )

    def get(self, *args, **kwargs):
        if not self.request.query_params.get("test"):
            movies = MovieService.get_movies_from_imdb(kwargs.get("expression"))
            Movie.objects.bulk_create(
                [Movie(**asdict(movie)) for movie in movies],
                update_conflicts=True,
                unique_fields=['title'],
                update_fields=['imdb_id', 'poster', 'year', 'type', 'poster']
            )
        return super().get(*args, **kwargs)


class FindMovieAiView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    pagination_class = MoviesPagination
    throttle_classes = [AiSearchUaThrottle, AiSearchIpThrottle, AiSearchForwardedThrottle]

    def post(self, request, *args, **kwargs):

        input_serializer = FindMovieAiViewRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        prompt = input_serializer.data.get("prompt")
        ai_movies = FindMovieAiClient(prompt).find_movies()

        movies = []
        for ai_movie in ai_movies:
            imdb_movie = next(
                filter(lambda x: x.title == ai_movie.title, MovieService.get_movies_from_imdb(ai_movie.title)),
                None
            )
            if imdb_movie:
                movies.append(
                    Movie(
                        **asdict(imdb_movie),
                        genre=ai_movie.genre,
                        plot=ai_movie.plot,
                    )
                )
        Movie.objects.bulk_create(
            movies,
            update_conflicts=True,
            unique_fields=['title'],
            update_fields=['imdb_id', 'poster', 'year', 'type', 'poster', 'genre', 'plot']
        )
        serialized_movies = MovieSerializer(movies, many=True)
        return Response(serialized_movies.data, status=status.HTTP_200_OK)


class WatchLaterCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context


class WatchLaterListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterListSerializer
    pagination_class = MoviesPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = WatchLaterFilter
    search_fields = ['movie__title']
    ordering_fields = ['movie__title', 'movie__genre', 'movie__year']
    ordering = ['movie__title']

    def get_queryset(self):
        return (
            WatchLaterMovie.objects.filter(user_id=self.request.user.id)
            .select_related("movie")
            .annotate(
                likes_count=Count("movie__likemovie"),
                is_liked=Exists(
                    LikeMovie.objects.filter(
                        user_id=self.request.user.id, movie_id=OuterRef("movie__pk")
                    ),
                ),
                watch_later_count=Count("movie__watchlatermovie"),
                is_watch_later=Exists(
                    WatchLaterMovie.objects.filter(
                        user_id=self.request.user.id, movie_id=OuterRef("movie__pk")
                    ),
                ),
            )
        )


class WatchLaterDestroyView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        WatchLaterMovie.objects.filter(
            user_id=self.request.user.id, movie_id=kwargs.get("pk")
        ).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
