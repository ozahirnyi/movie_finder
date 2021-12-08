import json

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import FavoriteMovieUser


@login_required(login_url=settings.LOGIN_PAGE_URL)
def favorites(request):
    if request.method == 'GET':
        favorite_movies = FavoriteMovieUser.objects.filter(
                user=request.user).values()
        return render(request, 'finder/favorites.html', context={
            'favorite_movies': favorite_movies})
    else:
        return HttpResponse(status=501)


def add_to_favorites(movie, user):
    FavoriteMovieUser.objects.create(title=movie['Title'],
                                     imdb_id=movie['imdbID'],
                                     year=movie['Year'],
                                     type=movie['Type'],
                                     poster=movie['Poster'],
                                     user=user)


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
    if request.method == 'POST':
        movie_to_find = request.POST.get('movie_name_to_find')
        movie_to_favorites = request.POST.get('movie_to_favorites')
        if movie_to_find:
            context = find_movie(movie_to_find)
            return render(request, 'finder/index.html', context=context)
        if movie_to_favorites:
            add_to_favorites(eval(movie_to_favorites), request.user)
    return render(request, 'finder/index.html')


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
