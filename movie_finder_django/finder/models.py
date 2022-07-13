import json
import os

import requests
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count

from sql_log import query_debugger


class Movie(models.Model):
    title = models.CharField(max_length=128)
    imdb_id = models.CharField(max_length=128)
    wiki_link = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=16)
    type = models.CharField(max_length=128)
    poster = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @query_debugger
    @property
    def get_top_10(self):
        return {'movies': [UserFavorite.objects.annotate(
                               movie_count=Count('movie')).order_by(
                               'movie_count')]}

    @staticmethod
    def find_movie(expression):
        url = 'https://imdb-api.com/en/API/Search/'
        api_key = os.getenv('imdb_api_key')

        response = requests.get(url + api_key + '/' + expression)
        return json.loads(response.text)

    def __str__(self):
        return self.title


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_favorite_movies(user):
        return [user_favorite.movie for user_favorite in
                UserFavorite.objects.select_related('movie').filter(
                    user=user).order_by(
                    '-updated_at')]

    def __str__(self):
        return f'{self.user} | {self.movie}'
