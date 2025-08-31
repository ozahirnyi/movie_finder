import json
import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from .managers import MovieManager


class Actor(models.Model):
    full_name = models.CharField(max_length=128, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Director(models.Model):
    full_name = models.CharField(max_length=128, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Movie(models.Model):
    title = models.CharField(max_length=128, unique=True)
    imdb_id = models.CharField(max_length=128)
    wiki_link = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=16, null=True)
    type = models.CharField(max_length=128, null=True)
    poster = models.CharField(max_length=255, null=True)
    plot = models.TextField(null=True)

    genres = models.ManyToManyField(Genre, related_name='movies_genres')
    actors = models.ManyToManyField(Actor, related_name='movies_actors')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MovieManager.as_manager()

    class Meta:
        app_label = "movie"

    def __str__(self):
        return self.title


class UserMovie(models.Model):
    related_model = Movie
    related_model_field = "movie_id"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "movie"
        abstract = True

    def __str__(self):
        return f"{self.user} | {self.movie}"


class WatchLaterMovie(UserMovie):
    class Meta(UserMovie.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"], name="watchlater-user-movie-unique"
            )
        ]


class LikeMovie(UserMovie):
    class Meta(UserMovie.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"], name="like-user-movie-unique"
            )
        ]
