import json

import requests
from django.conf import settings

from .ai_find_movie import FindMovieAiClient
from .dataclasses import ImdbMovie, AiMovie


class MovieService:
    @staticmethod
    def get_movies_from_imdb(expression: str) -> list[ImdbMovie]:
        response = requests.get(
            settings.IMDB_API_URL + "?limit=1&query=" + expression,
            headers={'authorization': settings.IMDB_API_KEY, 'content-type': 'application/json'},
            timeout=10,
        )
        imdb_movies = []
        for data in json.loads(response.text)["result"]:
            imdb_movies.append(
                ImdbMovie(
                    title=data["Title"],
                    imdb_id=data["imdbID"],
                    poster=data["Poster"],
                    year=data["Year"],
                    type=data["Type"],
                )
            )
        return imdb_movies

    @staticmethod
    def get_movies_from_ai(expression: str) -> list[AiMovie]:
        return FindMovieAiClient(expression).find_movies()

