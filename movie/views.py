from dataclasses import asdict

from django.db import IntegrityError
from django.db.models import Count, OuterRef, Exists
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import permissions, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    GenericAPIView,
    DestroyAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from throttling.throttling import (
    RegularSearchUaThrottle,
    RegularSearchIpThrottle,
    RegularSearchForwardedThrottle,
    AiSearchUaThrottle,
    AiSearchIpThrottle,
    AiSearchForwardedThrottle,
)
from .ai_find_movie import FindMovieAiClient
from .errors import AddLikeError
from .filters import MovieFilter, WatchLaterFilter
from .models import Movie, WatchLaterMovie, LikeMovie, Director, Actor, Genre
from .paginations import MoviesPagination
from .serializers import (
    MovieSerializer,
    WatchLaterCreateSerializer,
    WatchLaterListSerializer,
    FindMovieAiViewRequestSerializer,
)
from .services import MovieService


class MovieView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    lookup_field = "id"

    def get_queryset(self):
        return (
            Movie.objects.with_is_liked(self.request.user.id)
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
    throttle_classes = [
        RegularSearchUaThrottle,
        RegularSearchIpThrottle,
        RegularSearchForwardedThrottle,
    ]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ["title"]
    ordering_fields = ["imdb_id", "title", "genre", "year", "likes_count"]
    ordering = ["imdb_id"]

    def get_queryset(self):
        queryset = Movie.objects.all()
        if expression := self.request.query_params.get("expression"):
            queryset = queryset.filter(title__icontains=expression)
        return (
            queryset.with_is_liked(self.request.user.id)
            .with_is_watch_later(self.request.user.id)
            .with_likes_count()
            .with_watch_later_count()
        )

    @extend_schema(parameters=[OpenApiParameter(name="expression", type=str, location=OpenApiParameter.QUERY)])
    def get(self, *args, **kwargs):
        if expression := self.request.query_params.get("expression"):
            movies = MovieService.get_movies_from_imdb(expression)
            Movie.objects.bulk_create(
                [Movie(**asdict(movie)) for movie in movies],
                update_conflicts=True,
                unique_fields=["title"],
                update_fields=["imdb_id", "poster", "year", "type"],
            )
        return super().get(*args, **kwargs)


class FindMovieAiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MovieSerializer
    throttle_classes = [
        AiSearchUaThrottle,
        AiSearchIpThrottle,
        AiSearchForwardedThrottle,
    ]

    @extend_schema(
        request=FindMovieAiViewRequestSerializer,
        responses={status.HTTP_200_OK: MovieSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        # TODO: Move this to a service
        input_serializer = FindMovieAiViewRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        ai_movies = FindMovieAiClient(**input_serializer.data).find_movies()
        for ai_movie in ai_movies:
            imdb_movie = next(
                filter(
                    lambda x: x.title == ai_movie.title,
                    MovieService.get_movies_from_imdb(ai_movie.title),
                ),
                None,
            )
            ai_movie.poster = imdb_movie.poster

        director_names = {m.director for m in ai_movies}
        genre_names = {g for m in ai_movies for g in m.genre}
        actor_names = {a for m in ai_movies for a in m.actors}

        existing_directors = {d.full_name: d for d in Director.objects.filter(full_name__in=director_names)}
        existing_genres = {g.name: g for g in Genre.objects.filter(name__in=genre_names)}
        existing_actors = {a.full_name: a for a in Actor.objects.filter(full_name__in=actor_names)}

        new_directors = [Director(full_name=name) for name in director_names if name not in existing_directors]
        new_genres = [Genre(name=name) for name in genre_names if name not in existing_genres]
        new_actors = [Actor(full_name=name) for name in actor_names if name not in existing_actors]

        Director.objects.bulk_create(new_directors)
        Genre.objects.bulk_create(new_genres)
        Actor.objects.bulk_create(new_actors)

        existing_directors.update({d.full_name: d for d in Director.objects.filter(full_name__in=director_names)})
        existing_genres.update({g.name: g for g in Genre.objects.filter(name__in=genre_names)})
        existing_actors.update({a.full_name: a for a in Actor.objects.filter(full_name__in=actor_names)})

        movies = []
        for ai_movie in ai_movies:
            movie = Movie(
                title=ai_movie.title,
                imdb_id=ai_movie.imdb_id,
                poster=ai_movie.poster,
                year=ai_movie.year,
                type=ai_movie.type,
                plot=ai_movie.plot,
                director=existing_directors[ai_movie.director],
            )
            movies.append((movie, ai_movie.genre, ai_movie.actors))

        Movie.objects.bulk_create(
            [m for m, _, _ in movies],
            update_conflicts=True,
            unique_fields=["title"],
            update_fields=["imdb_id", "poster", "year", "type", "plot"],
        )

        for movie, genres, actors in movies:
            movie.genres.set([existing_genres[g] for g in genres])
            movie.actors.set([existing_actors[a] for a in actors])

        serialized_movies = MovieSerializer([m for m, _, _ in movies], many=True)
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
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = WatchLaterFilter
    search_fields = ["movie__title"]
    ordering_fields = ["movie__imdb_id", "movie__title", "movie__genre", "movie__year"]
    ordering = ["movie__imdb_id"]

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
