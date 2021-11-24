from django.shortcuts import render
from .models import Movie
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    movies = Movie.objects.filter()
    return render(request, 'finder/index.html', context={'movies': movies})

