import datetime

import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User


class FavoriteMovieUser(models.Model):
    title = models.CharField(max_length=128)
    imdb_id = models.CharField(max_length=128)
    wiki_link = models.CharField(max_length=255)
    year = models.CharField(max_length=16)
    type = models.CharField(max_length=128)
    poster = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
