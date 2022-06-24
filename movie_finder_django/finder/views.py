import json

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sql_log import query_debugger
from .forms import CustomUserCreationForm
from .models import UserFavorite, Movie


@query_debugger
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


def find_movie(movie_to_find):
    querystring = {'s': movie_to_find, 'r': 'json'}
    headers = {
        'x-rapidapi-host': settings.KOSTILNIE_VARIABLES[
            'X_RAPIDAPI_HOST'],
        'x-rapidapi-key': settings.KOSTILNIE_VARIABLES[
            'X_RAPIDAPI_KEY']
    }
    response = json.loads(
        requests.request("GET", settings.IMDB_API_URL, headers=headers,
                         params=querystring).text)
    context = {'movies': response['Search']} if response.get(
        'Search') else {
        'messages': ['There are no any info for your request']}
    return context


@login_required(login_url=settings.LOGIN_PAGE_URL)
def index(request):
    movie_to_find = request.POST.get('movie_name_to_find')
    if movie_to_find:
        context = find_movie(movie_to_find)
        return render(request, 'finder/index.html', context=context)
    else:
        a = Movie.get_top_10()
        return render(request, 'finder/index.html',
                      context=Movie.get_top_10())


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
