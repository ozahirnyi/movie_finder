from django.contrib import admin
from .models import UserFavorite, Movie

admin.register(UserFavorite)(admin.ModelAdmin)
admin.register(Movie)(admin.ModelAdmin)
