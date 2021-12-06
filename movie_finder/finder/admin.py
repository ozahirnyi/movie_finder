from django.contrib import admin
from .models import FavoriteMovieUser

admin.register(FavoriteMovieUser)(admin.ModelAdmin)
