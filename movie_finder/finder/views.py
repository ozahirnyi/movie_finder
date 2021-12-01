import json

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


@login_required(login_url=settings.LOGIN_PAGE_URL)
def favorites(request):
    return render(request, 'finder/favorites.html')


@login_required(login_url=settings.LOGIN_PAGE_URL)
def index(request):
    if request.method == 'POST':
        movie_to_find = request.POST['movie_name_to_find']
        querystring = {"s": movie_to_find, "r": "json"}
        headers = {
            'x-rapidapi-host': settings.KOSTILNIE_VARIABLES[
                'X_RAPIDAPI_HOST'],
            'x-rapidapi-key': settings.KOSTILNIE_VARIABLES[
                'X_RAPIDAPI_KEY']
        }
        response = json.loads(requests.request("GET", settings.IMDB_API_URL, headers=headers,
                                               params=querystring).text)
        context = {'movies': response['Search']} if response.get('Search') else {
            'messages': ['There are no any info for your request']}
        return render(request, 'finder/index.html', context=context)
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
