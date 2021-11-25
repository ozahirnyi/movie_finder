from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import Movie
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    movies = Movie.objects.filter()
    return render(request, 'finder/index.html', context={'movies': movies})



def registration(request):
    if request.POST == 'POST':
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
            return render(request, 'finder/index.html')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)
