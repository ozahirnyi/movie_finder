from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.filter()
    return render(request, 'index.html', context={'movies': movies})

