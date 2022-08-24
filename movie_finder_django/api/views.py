from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .errors import FindMovieNotExist
from .models import UserFavorite, Movie
from .serializers import MovieSerializer


def favorites_by_imdb_id(request, imdb_id):
    if request.method == 'DELETE':
        UserFavorite.objects.filter(
            user=request.user,
            movie__imdb_id=imdb_id,
        ).delete()
        return HttpResponse("Removed successful", status=200)


def add_to_favorites(movie, user):
    try:
        movie_to_favorite = Movie.objects.get(imdb_id=movie['imdbID'])
    except Movie.DoesNotExist:
        movie_to_favorite = Movie.objects.create(
            title=movie['Title'],
            imdb_id=movie['imdbID'],
            year=movie['Year'],
            type=movie['Type'],
            poster=movie['Poster'],
        )
    UserFavorite.objects.create(user=user, movie=movie_to_favorite)


class FindMovieView(GenericAPIView):
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer

    def get(self, *args, **kwargs):
        if expression := kwargs.get('expression'):
            movies = Movie.objects.filter(title__regex=expression)
            if not movies.exists():
                movies = Movie.find_movie(expression)
                if len(movies) == 0:
                    raise FindMovieNotExist
            data = self.get_serializer(movies, many=True).data
            return Response(data)
