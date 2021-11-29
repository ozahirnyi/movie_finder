from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import Movie


@login_required(login_url='/login/')
def index(request):
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
            return render(request, 'finder/index.html')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)
