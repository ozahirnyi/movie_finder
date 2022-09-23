import json
from typing import List, Optional

import regex
import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint

from api.errors import FindMovieNotExist


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
        pass

    @staticmethod
    def get_movies_from_imdb(expression: str) -> Optional[List[int]]:
        response = requests.get(settings.IMDB_API_URL + settings.IMDB_API_KEY + '/' + expression)
        parsed_response = json.loads(response.text)['results']
        movie_ids = []

        if not parsed_response:
            raise FindMovieNotExist

        for data in parsed_response:
            description = regex.sub(r'\(|\)', '', data['description']).split(' ', 1)
            movie = Movie.objects.update_or_create(
                title=data['title'],
                imdb_id=data['id'],
                poster=data['image'],
                year=description[0] if len(description) > 0 else None,
                type=description[1] if len(description) > 1 else None,
            )
            movie_ids.append(movie[0].id)
        # TODO: uncomment when start use postgresql. > movie_finder_django/api/tests.py
        # Movie.objects.bulk_create(movies)
        return movie_ids

    def __str__(self):
        return self.title


class UserMovie(models.Model):
    related_model = Movie
    related_model_field = 'movie_id'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'
        abstract = True
        # constraints = [
        #     models.UniqueConstraint(fields=['user', 'movie'], name="%%(class)-user-movie-unique")
        # ]
        # unique_together = ("user", "movie")

    def __str__(self):
        return f'{self.user} | {self.movie}'


class WatchLaterMovie(UserMovie):
    pass


class LikeMovie(UserMovie):
    class Meta(UserMovie.Meta):
        constraints = [
            models.UniqueConstraint(fields=['user', 'movie'], name='like-user-movie-unique')
        ]
