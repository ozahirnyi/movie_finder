from rest_framework import permissions
from rest_framework.generics import GenericAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response

from .errors import FindMovieNotExist
from .models import Movie, WatchLater
from .serializers import MovieSerializer, WatchLaterSerializer, WatchLaterCreateSerializer


class FindMovieView(GenericAPIView):
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer

    def get(self, *args, **kwargs):
        expression = kwargs.get('expression')

        movies = Movie.objects.filter(title__regex=expression)
        if not movies.exists():
            movies = Movie.find_movie(expression)
            if len(movies) == 0:
                raise FindMovieNotExist
        data = self.get_serializer(movies, many=True).data
        return Response(data)


class WatchLaterCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class WatchLaterListView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterSerializer

    def get(self, *args, **kwargs):
        watch_later = WatchLater.objects.filter(user=self.request.user)
        serializer = self.get_serializer(data=watch_later, many=True)
        serializer.is_valid()

        return Response(serializer.data)


class WatchLaterDestroyView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterSerializer
    queryset = WatchLater.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
