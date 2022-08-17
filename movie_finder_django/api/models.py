import json

import regex
import requests
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count

from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=128)
    imdb_id = models.CharField(max_length=128)
    wiki_link = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=16, null=True)
    type = models.CharField(max_length=128, null=True)
    poster = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'

    @property
    def get_top_10(self):
        return {'movies': [UserFavorite.objects.annotate(
                               movie_count=Count('movie')).order_by(
                               'movie_count')]}

    @staticmethod
    def find_movie(expression):
        response = requests.get(settings.IMDB_API_URL + settings.IMDB_API_KEY + '/' + expression)
        parsed_response = json.loads(response.text)
        movies = []

        for data in parsed_response['results']:
            description = regex.sub(r'\(|\)', '', data['description']).split(' ', 1)
            movie = Movie.objects.create(
                title=data['title'],
                imdb_id=data['id'],
                poster=data['image'],
                year=description[0] if len(description) > 0 else None,
                type=description[1] if len(description) > 1 else None,
            )
            movies.append(movie)
        return movies

    def __str__(self):
        return self.title


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'

    @staticmethod
    def get_favorite_movies(user):
        return [user_favorite.movie for user_favorite in
                UserFavorite.objects.select_related('movie').filter(
                    user=user).order_by(
                    '-updated_at')]

    def __str__(self):
        return f'{self.user} | {self.movie}'
