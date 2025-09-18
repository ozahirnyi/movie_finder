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


class Language(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Writer(models.Model):
    full_name = models.CharField(max_length=128, unique=True)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    imdb_id = models.CharField(max_length=128, unique=True)
    year = models.CharField(max_length=16, blank=True)
    released_date = models.DateField(null=True, blank=True)
    runtime = models.CharField(max_length=32, blank=True)
    plot = models.TextField(blank=True)
    awards = models.TextField(blank=True)
    poster = models.CharField(max_length=255, blank=True)
    metascore = models.CharField(max_length=16, blank=True)
    imdb_rating = models.CharField(max_length=16, blank=True)
    imdb_votes = models.CharField(max_length=32, blank=True)
    type = models.CharField(max_length=128, blank=True)
    total_seasons = models.CharField(max_length=16, blank=True)

    genres = models.ManyToManyField(Genre, related_name='movies_genres')
    actors = models.ManyToManyField(Actor, related_name='movies_actors')
    directors = models.ManyToManyField(Director, related_name='movies_directors')
    countries = models.ManyToManyField(Country, related_name='movies_countries')
    languages = models.ManyToManyField(Language, related_name='movies_languages')
    writers = models.ManyToManyField(Writer, related_name='movies_writers')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MovieManager.as_manager()

    class Meta:
        app_label = 'movie'

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_ratings')
    source = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)


class UserMovie(models.Model):
    related_model = Movie
    related_model_field = 'movie_id'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'movie'
        abstract = True

    def __str__(self):
        return f'{self.user} | {self.movie}'


class WatchLaterMovie(UserMovie):
    class Meta(UserMovie.Meta):
        constraints = [models.UniqueConstraint(fields=['user', 'movie'], name='watchlater-user-movie-unique')]


class LikeMovie(UserMovie):
    class Meta(UserMovie.Meta):
        constraints = [models.UniqueConstraint(fields=['user', 'movie'], name='like-user-movie-unique')]
