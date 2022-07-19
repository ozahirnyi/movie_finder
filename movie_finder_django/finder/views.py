import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from errors import FindMovieNotExist
from serializers import MovieSerializer
from .forms import CustomUserCreationForm
from .models import UserFavorite, Movie


@login_required(login_url=settings.LOGIN_PAGE_URL)
def favorites(request):
    if request.method == 'GET':
        return render(request, 'finder/favorites.html', context={
            'favorite_movies': UserFavorite.get_favorite_movies(
                request.user)})
    elif request.method == 'POST':
        movie = request.POST.get('movie')
        if movie:
            add_to_favorites(json.loads(movie), request.user)
            return HttpResponse("Add successful", status=201)
        else:
            return HttpResponse("Bad movie data", status=204)


def favorites_by_imdb_id(request, imdb_id):
    if request.method == 'DELETE':
        UserFavorite.objects.filter(user=request.user,
                                    movie__imdb_id=imdb_id).delete()
        return HttpResponse("Removed successful", status=200)


def add_to_favorites(movie, user):
    try:
        movie_to_favorite = Movie.objects.get(imdb_id=movie['imdbID'])
    except Movie.DoesNotExist:
        movie_to_favorite = Movie.objects.create(title=movie['Title'],
                                                 imdb_id=movie['imdbID'],
                                                 year=movie['Year'],
                                                 type=movie['Type'],
                                                 poster=movie['Poster'])
    UserFavorite.objects.create(user=user, movie=movie_to_favorite)


class FindMovieView(GenericAPIView):
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticated]
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


@login_required(login_url=settings.LOGIN_PAGE_URL)
def index(request):
    movie_to_find = request.POST.get('movie_name_to_find')
    if movie_to_find:
        context = Movie.find_movie(movie_to_find)
        return HttpResponse(context)
    else:
        a = Movie.get_top_10
        return render(request, 'finder/index.html',
                      context=Movie.get_top_10)


def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data['username'],
                form.data.get('email'),
                form.cleaned_data['password1']
            )
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)
