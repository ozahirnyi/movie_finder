import os

import django.conf
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import Movie


@login_required(login_url='/login/')
def index(request):
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"s": "Avengers Endgame", "page": "1", "r": "json"}
    headers = {
        'x-rapidapi-host': django.conf.settings.KOSTILNIE_VARIABLES[
            'X_RAPIDAPI_HOST'],
        'x-rapidapi-key': django.conf.settings.KOSTILNIE_VARIABLES[
            'X_RAPIDAPI_KEY']
    }
    response = requests.request("GET", url, headers=headers,
                                params=querystring)
    movies = Movie.objects.filter()
    return render(request, 'finder/index.html', context={'movies': movies})


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
