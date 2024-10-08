from django.db import IntegrityError
from django.db.models import Count, OuterRef, Exists
from rest_framework import permissions, status
from rest_framework.generics import (
    GenericAPIView,
    DestroyAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from .errors import AddLikeError
from .models import Movie, WatchLaterMovie, LikeMovie
from .paginations import MoviesPagination
from .serializers import (
    MovieSerializer,
    WatchLaterCreateSerializer,
    WatchLaterListSerializer,
)
from .ai_find_movie import FindMovieAiClient

from .services import MovieService


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

    def get_queryset(self):
        return (
            Movie.objects
            .filter(title__icontains=self.kwargs.get("expression"))
            .with_is_liked(self.request.user.id)
            .with_is_watch_later(self.request.user.id)
            .with_likes_count()
            .with_watch_later_count()
        )

    def get(self, *args, **kwargs):
        # Get from imdb and save to db
        if not self.request.query_params.get("test"):
            MovieService.get_movies_from_imdb(kwargs.get("expression"))
        return super().get(*args, **kwargs)


class FindMovieAiView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    pagination_class = MoviesPagination

    def post(self, request, *args, **kwargs):
        if prompt := self.request.data.get("prompt"):
            movies = FindMovieAiClient(prompt).find_movies()
        return Response(status=status.HTTP_200_OK)


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

    def get_queryset(self):
        return (
            WatchLaterMovie.objects.filter(user_id=self.request.user)
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
    queryset = WatchLaterMovie.objects.all()
