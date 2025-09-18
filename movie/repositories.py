import json
from datetime import datetime

import requests
from django.conf import settings
from django.db import transaction

from movie.dataclasses import (
    Actor as ActorDTO,
)
from movie.dataclasses import (
    Country as CountryDTO,
)
from movie.dataclasses import (
    Director as DirectorDTO,
)
from movie.dataclasses import (
    Genre as GenreDTO,
)
from movie.dataclasses import (
    ImdbMovie,
    OmdbMovie,
)
from movie.dataclasses import (
    Language as LanguageDTO,
)
from movie.dataclasses import (
    Rating as RatingDTO,
)
from movie.dataclasses import (
    Writer as WriterDTO,
)
from movie.models import Actor, Country, Director, Genre, Language, Movie, Rating, Writer


class MovieRepository:
    def get_movies_from_imdb(self, expression: str) -> list[ImdbMovie]:
        response = requests.get(
            settings.IMDB_API_SEARCH_BY_NAME_URL + '?query=' + expression,
            headers={
                'authorization': settings.IMDB_API_KEY,
                'content-type': 'application/json',
            },
            timeout=30,
        )
        imdb_movies = []
        for data in json.loads(response.text)['result']:
            imdb_movies.append(
                ImdbMovie(
                    title=data['Title'],
                    imdb_id=data['imdbID'],
                    poster=data['Poster'],
                    year=data['Year'],
                    type=data['Type'],
                )
            )
        return imdb_movies

    @staticmethod
    def get_movie_from_omdb_by_expression(title: str) -> OmdbMovie:
        try:
            response = requests.get(
                f'{settings.OMDB_API_URL}?t={title}&apikey={settings.OMDB_API_KEY}',
                headers={'content-type': 'application/json'},
                timeout=30,
            )
            data = response.json()
            omdb_movie = OmdbMovie(
                title=data.get('Title'),
                year=data.get('Year'),
                released_date=datetime.strptime(data['Released'], '%d %b %Y').date() if data.get('Released') else None,
                runtime=data.get('Runtime'),
                genres=[Genre(name=name.strip()) for name in data.get('Genre', '').split(',') if name.strip()],
                directors=[Director(full_name=name.strip()) for name in data.get('Director', '').split(',') if name.strip()],
                writers=[Writer(full_name=name.strip()) for name in data.get('Writer', '').split(',') if name.strip()],
                actors=[Actor(full_name=name.strip()) for name in data.get('Actors', '').split(',') if name.strip()],
                plot=data.get('Plot'),
                languages=[Language(name=name.strip()) for name in data.get('Language', '').split(',') if name.strip()],
                countries=[Country(name=name.strip()) for name in data.get('Country', '').split(',') if name.strip()],
                awards=data.get('Awards'),
                poster=data.get('Poster'),
                ratings=[Rating(source=rating['Source'], value=rating['Value']) for rating in data.get('Ratings', [])],
                metascore=data.get('Metascore'),
                imdb_rating=data.get('imdbRating'),
                imdb_votes=data.get('imdbVotes'),
                imdb_id=data.get('imdbID'),
                type=data.get('Type'),
                total_seasons=data.get('totalSeasons'),
            )
            return omdb_movie
        except Exception as e:
            raise Exception(f'Error while getting movies from OMDB: {e}')

    def _create_movie_in_db(self, omdb_movie: OmdbMovie) -> Movie:
        with transaction.atomic():
            movie_instance, created = Movie.objects.get_or_create(
                imdb_id=omdb_movie.imdb_id,
                defaults={
                    'title': omdb_movie.title,
                    'year': omdb_movie.year,
                    'released_date': omdb_movie.released_date,
                    'runtime': omdb_movie.runtime,
                    'plot': omdb_movie.plot,
                    'awards': omdb_movie.awards,
                    'poster': omdb_movie.poster,
                    'metascore': omdb_movie.metascore,
                    'imdb_rating': omdb_movie.imdb_rating,
                    'imdb_votes': omdb_movie.imdb_votes,
                    'type': omdb_movie.type,
                    'total_seasons': omdb_movie.total_seasons,
                },
            )
            if created:
                if omdb_movie.genres:
                    genres = [Genre.objects.get_or_create(name=genre.name)[0] for genre in omdb_movie.genres]
                    movie_instance.genres.set(genres)
                if omdb_movie.actors:
                    actors = [Actor.objects.get_or_create(full_name=actor.full_name)[0] for actor in omdb_movie.actors]
                    movie_instance.actors.set(actors)
                if omdb_movie.directors:
                    directors_list = [Director.objects.get_or_create(full_name=director.full_name)[0] for director in omdb_movie.directors]
                    movie_instance.directors.set(directors_list)
                if omdb_movie.ratings:
                    ratings = [Rating(source=rating.source, value=rating.value, movie_id=movie_instance.id) for rating in omdb_movie.ratings]
                    Rating.objects.bulk_create(ratings)
                if omdb_movie.languages:
                    languages = [Language.objects.get_or_create(name=language.name)[0] for language in omdb_movie.languages]
                    movie_instance.languages.set(languages)
                if omdb_movie.countries:
                    countries = [Country.objects.get_or_create(name=country.name)[0] for country in omdb_movie.countries]
                    movie_instance.countries.set(countries)
                if omdb_movie.writers:
                    writers = [Writer.objects.get_or_create(full_name=writer.full_name)[0] for writer in omdb_movie.writers]
                    movie_instance.writers.set(writers)
            return movie_instance

    def search_movies_in_omdb(self, movie_titles: list[str], initiator_id: int) -> list[OmdbMovie]:
        search_results = []
        for title in movie_titles:
            movie_instance = (
                Movie.objects.filter(title=title)
                .with_is_liked(initiator_id)
                .with_is_watch_later(initiator_id)
                .with_likes_count()
                .with_watch_later_count()
                .first()
            )
            if not movie_instance:
                omdb_movie = self.get_movie_from_omdb_by_expression(title)
                self._create_movie_in_db(omdb_movie)
            else:
                omdb_movie = OmdbMovie(
                    title=movie_instance.title,
                    year=movie_instance.year,
                    released_date=movie_instance.released_date,
                    runtime=movie_instance.runtime,
                    genres=[GenreDTO(genre.name) for genre in movie_instance.genres.all()],
                    directors=[DirectorDTO(director.full_name) for director in movie_instance.directors.all()],
                    writers=[WriterDTO(writer.full_name) for writer in movie_instance.writers.all()],
                    actors=[ActorDTO(actor.full_name) for actor in movie_instance.actors.all()],
                    plot=movie_instance.plot,
                    languages=[LanguageDTO(language.name) for language in movie_instance.languages.all()],
                    countries=[CountryDTO(country.name) for country in movie_instance.countries.all()],
                    awards=movie_instance.awards,
                    poster=movie_instance.poster,
                    ratings=[RatingDTO(source=rating.source, value=rating.value) for rating in movie_instance.movie_ratings.all()],
                    metascore=movie_instance.metascore,
                    imdb_rating=movie_instance.imdb_rating,
                    imdb_votes=movie_instance.imdb_votes,
                    imdb_id=movie_instance.imdb_id,
                    type=movie_instance.type,
                    total_seasons=movie_instance.total_seasons,
                )
            search_results.append(omdb_movie)
        return search_results
