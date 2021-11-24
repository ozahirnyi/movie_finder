from django.contrib import admin
from .models import Actor, Movie

admin.register(Actor)(admin.ModelAdmin)
admin.register(Movie)(admin.ModelAdmin)
