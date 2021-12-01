import json

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import Movie


@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        movie_to_find = request.POST['movie_name_to_find']
        url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
        querystring = {"s": movie_to_find, "r": "json"}
        headers = {
            'x-rapidapi-host': settings.KOSTILNIE_VARIABLES[
                'X_RAPIDAPI_HOST'],
            'x-rapidapi-key': settings.KOSTILNIE_VARIABLES[
                'X_RAPIDAPI_KEY']
        }
        response = requests.request("GET", url, headers=headers,
                                    params=querystring)
        try:
            movies = json.loads(response.text)['Search']
            return render(request, 'finder/index.html', context={'movies': movies})
        except KeyError:
            return render(request, 'finder/index.html')
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
