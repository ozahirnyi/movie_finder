import json
from datetime import date
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase

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
    Language as LanguageDTO,
)
from movie.dataclasses import (
    OmdbMovie,
)
from movie.dataclasses import (
    Rating as RatingDTO,
)
from movie.dataclasses import (
    Writer as WriterDTO,
)
from movie.models import Actor, Country, Director, Genre, Language, Movie, Rating, RecommendedMovie, Writer
from movie.repositories import MovieRepository, RecommendationRepository
from movie.services import MovieService


class MovieRepositoryTests(TestCase):
    def setUp(self):
        self.repository = MovieRepository()

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_imdb_parses_payload(self, mock_get):
        mock_get.return_value.text = json.dumps(
            {
                'result': [
                    {'Title': 'Shrek', 'imdbID': 'tt0126029', 'Poster': 'poster', 'Year': '2001', 'Type': 'movie'},
                ]
            }
        )

        movies = self.repository.get_movies_from_imdb('shrek')

        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].imdb_id, 'tt0126029')
        mock_get.assert_called_once()

    @patch('movie.repositories.requests.get')
    def test_get_movie_from_omdb_by_expression_builds_dataclass(self, mock_get):
        mock_get.return_value.json.return_value = {
            'Title': 'Shrek',
            'Year': '2001',
            'Released': '22 Apr 2001',
            'Runtime': '90 min',
            'Genre': 'Animation, Comedy',
            'Director': 'Andrew Adamson',
            'Writer': 'Ted Elliott',
            'Actors': 'Mike Myers',
            'Plot': 'Plot',
            'Language': 'English',
            'Country': 'USA',
            'Awards': 'Oscar',
            'Poster': 'poster',
            'Ratings': [{'Source': 'Internet', 'Value': '9/10'}],
            'Metascore': '80',
            'imdbRating': '8.5',
            'imdbVotes': '1000',
            'imdbID': 'tt0126029',
            'Type': 'movie',
            'totalSeasons': '1',
        }

        movie = self.repository.get_movie_from_omdb_by_expression('Shrek')

        self.assertEqual(movie.title, 'Shrek')
        self.assertEqual(movie.directors[0].full_name, 'Andrew Adamson')
        self.assertEqual(movie.ratings[0].value, '9/10')

    @patch('movie.repositories.requests.get', side_effect=RuntimeError('boom'))
    def test_get_movie_from_omdb_by_expression_wraps_errors(self, _):
        with self.assertRaises(Exception) as exc:
            self.repository.get_movie_from_omdb_by_expression('Shrek')

        self.assertIn('Error while getting movies from OMDB', str(exc.exception))

    def test_create_movie_in_db_sets_relations(self):
        omdb_movie = OmdbMovie(
            title='Brand New',
            imdb_id='tt999001',
            year='2024',
            released_date=date(2024, 1, 1),
            runtime='120 min',
            plot='Plot',
            genres=[GenreDTO(name='Adventure')],
            directors=[DirectorDTO(full_name='Director One')],
            writers=[WriterDTO(full_name='Writer One')],
            actors=[ActorDTO(full_name='Actor One')],
            languages=[LanguageDTO(name='English')],
            countries=[CountryDTO(name='USA')],
            awards='Awards',
            poster='Poster',
            ratings=[RatingDTO(source='Internet', value='10/10')],
            metascore='80',
            imdb_rating='9.0',
            imdb_votes='1000',
            type='movie',
            total_seasons='1',
        )

        movie = self.repository._create_movie_in_db(omdb_movie)

        self.assertEqual(movie.title, 'Brand New')
        self.assertEqual(movie.genres.first().name, 'Adventure')
        self.assertEqual(movie.movie_ratings.first().value, '10/10')
        self.assertEqual(movie.languages.first().name, 'English')
        self.assertEqual(movie.countries.first().name, 'USA')

    @patch.object(MovieRepository, 'get_movie_from_omdb_by_expression')
    def test_search_movies_in_omdb_handles_existing_and_new(self, mock_get_movie):
        genre = Genre.objects.create(name='Comedy')
        director = Director.objects.create(full_name='Director Existing')
        actor = Actor.objects.create(full_name='Actor Existing')
        writer = Writer.objects.create(full_name='Writer Existing')
        country = Country.objects.create(name='USA')
        language = Language.objects.create(name='English')

        existing = Movie.objects.create(title='Existing', imdb_id='tt000001')
        existing.genres.add(genre)
        existing.directors.add(director)
        existing.actors.add(actor)
        existing.writers.add(writer)
        existing.countries.add(country)
        existing.languages.add(language)
        Rating.objects.create(movie=existing, source='Internet', value='9.0')

        new_movie = OmdbMovie(
            title='Brand',
            imdb_id='tt000002',
            year='2024',
            type='movie',
            runtime='90 min',
            plot='Plot',
            awards='Awards',
            poster='poster',
            metascore='70',
            imdb_rating='8.0',
            imdb_votes='500',
            total_seasons='1',
            genres=[GenreDTO(name='Adventure')],
            directors=[DirectorDTO(full_name='Director New')],
            writers=[WriterDTO(full_name='Writer New')],
            actors=[ActorDTO(full_name='Actor New')],
            countries=[CountryDTO(name='Canada')],
            languages=[LanguageDTO(name='French')],
            ratings=[RatingDTO(source='Web', value='8/10')],
        )
        mock_get_movie.return_value = new_movie

        user = get_user_model().objects.create_user(email='search@test.test', password='validpass')

        results = self.repository.search_movies_in_omdb(['Existing', 'Brand'], initiator_id=user.id)

        returned_titles = [movie.title for movie in results]
        self.assertIn('Existing', returned_titles)
        self.assertIn('Brand', returned_titles)
        self.assertTrue(Movie.objects.filter(imdb_id='tt000002').exists())

        existing_entry = next(movie for movie in results if movie.title == 'Existing')
        self.assertEqual(existing_entry.id, existing.id)

        new_entry = next(movie for movie in results if movie.title == 'Brand')
        created_movie = Movie.objects.get(imdb_id='tt000002')
        self.assertEqual(new_entry.id, created_movie.id)


class MovieServiceTests(TestCase):
    def test_service_delegates_to_repository(self):
        service = MovieService()
        with patch.object(MovieRepository, 'get_movies_from_imdb', return_value=['movie']) as mock_imdb:
            self.assertEqual(service.get_movies_from_imdb('query'), ['movie'])
            mock_imdb.assert_called_once_with('query')

        with patch.object(MovieRepository, 'get_movie_from_omdb_by_expression', return_value='movie') as mock_omdb:
            self.assertEqual(service.get_movie_from_omdb_by_expression('title'), 'movie')
            mock_omdb.assert_called_once_with('title')

        with patch.object(MovieRepository, 'search_movies_in_omdb', return_value=['movie']) as mock_search:
            self.assertEqual(service.search_movies_in_omdb(['a'], initiator_id=1), ['movie'])
            mock_search.assert_called_once_with(['a'], 1)

        with patch('movie.ai_find_movie.FindMovieAiClient.find_movies', return_value=['ai_movie']):
            self.assertEqual(service.get_movies_from_ai('prompt'), ['ai_movie'])


class RecommendationRepositoryTests(TestCase):
    def setUp(self):
        self.repository = RecommendationRepository()
        self.user = get_user_model().objects.create_user(email='recommend@test.test', password='pw123456789')
        self.today = date.today()

        self.movie_one = Movie.objects.create(title='One', imdb_id='tt001')
        self.movie_two = Movie.objects.create(title='Two', imdb_id='tt002')
        self.movie_three = Movie.objects.create(title='Three', imdb_id='tt003')

    def test_replace_cached_recommendations_marks_inactive_instead_of_delete(self):
        RecommendedMovie.objects.create(
            user=self.user,
            movie=self.movie_one,
            recommendation_date=self.today,
        )
        RecommendedMovie.objects.create(
            user=self.user,
            movie=self.movie_two,
            recommendation_date=self.today,
        )

        self.repository.replace_cached_recommendations(
            self.user.id,
            self.today,
            [self.movie_two.id, self.movie_three.id],
        )

        entries = RecommendedMovie.objects.filter(user=self.user, recommendation_date=self.today)
        self.assertEqual(entries.count(), 3)

        movie_one_entry = entries.get(movie=self.movie_one)
        movie_two_entry = entries.get(movie=self.movie_two)
        movie_three_entry = entries.get(movie=self.movie_three)

        self.assertFalse(movie_one_entry.is_active)
        self.assertIsNotNone(movie_one_entry.deactivated_at)

        self.assertTrue(movie_two_entry.is_active)
        self.assertIsNone(movie_two_entry.deactivated_at)

        self.assertTrue(movie_three_entry.is_active)

        cached_ids = self.repository.get_cached_movie_ids(self.user.id, self.today)
        self.assertCountEqual(cached_ids, [self.movie_two.id, self.movie_three.id])

        self.repository.replace_cached_recommendations(
            self.user.id,
            self.today,
            [self.movie_one.id],
        )

        movie_one_entry.refresh_from_db()
        movie_two_entry.refresh_from_db()
        movie_three_entry.refresh_from_db()

        self.assertTrue(movie_one_entry.is_active)
        self.assertIsNone(movie_one_entry.deactivated_at)

        self.assertFalse(movie_two_entry.is_active)
        self.assertFalse(movie_three_entry.is_active)

        cached_ids = self.repository.get_cached_movie_ids(self.user.id, self.today)
        self.assertEqual(set(cached_ids), {self.movie_one.id})

    def test_get_movies_by_ids_returns_empty_for_missing_ids(self):
        movies = self.repository.get_movies_by_ids([], self.user.id)

        self.assertEqual(movies, [])

    def test_get_movies_by_titles_returns_empty_for_missing_titles(self):
        movies = self.repository.get_movies_by_titles([], self.user.id)

        self.assertEqual(movies, [])
