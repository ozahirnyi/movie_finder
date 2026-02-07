import json
from datetime import date, timedelta
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from movie.dataclasses import (
    Actor as ActorDTO,
)
from movie.dataclasses import (
    AiMovie,
    ImdbMovie,
    OmdbMovie,
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
    Rating as RatingDTO,
)
from movie.dataclasses import (
    Writer as WriterDTO,
)
from movie.filters import MovieFilter
from movie.models import Actor, Country, Director, Genre, Language, LikeMovie, Movie, Rating, RecommendedMovie, TopMovie, Writer
from movie.repositories import MovieRepository, RecommendationRepository, TopMoviesRepository
from movie.services import MovieService, TopMoviesService


class MovieFilterTests(TestCase):
    def test_rating_filters_ignore_none(self):
        queryset = Movie.objects.all()
        filterset = MovieFilter(data={}, queryset=queryset)

        self.assertIs(filterset.filter_rating_min(queryset, 'rating_min', None), queryset)
        self.assertIs(filterset.filter_rating_max(queryset, 'rating_max', None), queryset)


class MovieRepositoryTests(TestCase):
    def setUp(self):
        self.repository = MovieRepository()

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_imdb_parses_payload(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = json.dumps(
            {
                'result': [
                    {'Title': 'Shrek', 'imdbID': 'tt0126029', 'Poster': 'poster', 'Year': '2001', 'Type': 'movie'},
                ]
            }
        )
        mock_response.raise_for_status = lambda: None

        movies = self.repository.get_movies_from_imdb('shrek')

        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].imdb_id, 'tt0126029')
        mock_get.assert_called_once()

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_imdb_handles_missing_result_key(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = json.dumps({})
        mock_response.raise_for_status = lambda: None

        movies = self.repository.get_movies_from_imdb('shrek')

        self.assertEqual(len(movies), 0)

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_imdb_handles_non_list_result(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = json.dumps({'result': 'not a list'})
        mock_response.raise_for_status = lambda: None

        movies = self.repository.get_movies_from_imdb('shrek')

        self.assertEqual(len(movies), 0)

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_imdb_handles_invalid_json(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = 'not valid json'
        mock_response.raise_for_status = lambda: None

        with self.assertRaises(Exception) as exc:
            self.repository.get_movies_from_imdb('shrek')

        self.assertIn('Invalid JSON response', str(exc.exception))

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_imdb_handles_invalid_items_in_array(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.text = json.dumps(
            {
                'result': [
                    {'Title': 'Shrek', 'imdbID': 'tt0126029', 'Poster': 'poster', 'Year': '2001', 'Type': 'movie'},
                    'not a dict',
                    123,
                    None,
                ]
            }
        )
        mock_response.raise_for_status = lambda: None

        movies = self.repository.get_movies_from_imdb('shrek')

        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].imdb_id, 'tt0126029')

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_imdb_skips_items_that_raise_type_error(self, mock_get):
        class BadDict(dict):
            @property
            def get(self):  # type: ignore[override]
                raise TypeError('boom')

        mock_response = mock_get.return_value
        mock_response.text = json.dumps(
            {
                'result': [
                    {'Title': 'Shrek', 'imdbID': 'tt0126029', 'Poster': 'poster', 'Year': '2001', 'Type': 'movie'},
                ]
            }
        )
        # Replace parsed JSON with a list that contains a dict-like object whose .get raises TypeError.
        parsed = json.loads(mock_response.text)
        parsed['result'].append(BadDict({'Title': 'Bad'}))
        mock_response.raise_for_status = lambda: None

        # Patch json.loads inside the repository so we can inject our BadDict instance.
        with patch('movie.repositories.json.loads', return_value=parsed):
            movies = self.repository.get_movies_from_imdb('shrek')

        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].imdb_id, 'tt0126029')

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

    @patch('movie.repositories.requests.get')
    def test_get_movie_from_omdb_by_expression_converts_not_available_to_none(self, mock_get):
        mock_get.return_value.json.return_value = {
            'Title': 'Mystery',
            'Year': 'N/A',
            'Released': 'N/A',
            'Runtime': 'N/A',
            'Genre': 'N/A',
            'Director': 'N/A',
            'Writer': 'N/A',
            'Actors': 'N/A',
            'Plot': 'N/A',
            'Language': 'N/A',
            'Country': 'N/A',
            'Awards': 'N/A',
            'Poster': 'N/A',
            'Ratings': [{'Source': 'Internet', 'Value': 'N/A'}],
            'Metascore': 'N/A',
            'imdbRating': 'N/A',
            'imdbVotes': 'N/A',
            'imdbID': 'tt0000001',
            'Type': 'N/A',
            'totalSeasons': 'N/A',
        }

        movie = self.repository.get_movie_from_omdb_by_expression('Mystery')

        self.assertIsNone(movie.poster)
        self.assertIsNone(movie.runtime)
        self.assertIsNone(movie.imdb_rating)
        self.assertEqual(movie.genres, [])
        self.assertIsNone(movie.ratings[0].value)

    @patch('movie.repositories.requests.get')
    def test_get_movie_from_omdb_by_expression_returns_none_when_movie_not_found(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '{"Response":"False","Error":"Movie not found!"}'
        mock_get.return_value.json.return_value = {'Response': 'False', 'Error': 'Movie not found!'}

        result = self.repository.get_movie_from_omdb_by_expression('Unknown Title')

        self.assertIsNone(result)

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

    @patch.object(MovieRepository, 'get_movie_from_omdb_by_expression')
    def test_search_movies_in_omdb_excludes_when_omdb_returns_none(self, mock_get_movie):
        user = get_user_model().objects.create_user(email='skip@test.test', password='pass')
        valid = OmdbMovie(
            title='Found',
            imdb_id='tt000099',
            year='2024',
            type='movie',
            runtime='90 min',
            plot='P',
            awards='',
            poster='',
            metascore='70',
            imdb_rating='8.0',
            imdb_votes='100',
            total_seasons='',
            genres=[],
            directors=[],
            writers=[],
            actors=[],
            countries=[],
            languages=[],
            ratings=[],
        )

        def side_effect(title):
            return None if title == 'Not Found' else valid

        mock_get_movie.side_effect = side_effect
        results = self.repository.search_movies_in_omdb(['Not Found', 'Found'], initiator_id=user.id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Found')

    @patch.object(MovieRepository, 'get_movie_from_omdb_by_expression')
    def test_search_movies_in_omdb_skips_db_when_omdb_returns_no_imdb_id(self, mock_get_movie):
        omdb_no_imdb = OmdbMovie(
            title='Unknown',
            imdb_id='',
            year='2024',
            type='movie',
            runtime='',
            plot='',
            awards='',
            poster='',
            metascore='',
            imdb_rating='',
            imdb_votes='',
            total_seasons='',
            genres=[],
            directors=[],
            writers=[],
            actors=[],
            countries=[],
            languages=[],
            ratings=[],
        )
        mock_get_movie.return_value = omdb_no_imdb
        user = get_user_model().objects.create_user(email='noid@test.test', password='pass')
        results = self.repository.search_movies_in_omdb(['Unknown'], initiator_id=user.id)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Unknown')
        self.assertEqual(results[0].id, 0)
        self.assertFalse(Movie.objects.filter(title='Unknown').exists())

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_omdb_search_parses_search_response(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'Response': 'True',
            'Search': [
                {
                    'Title': 'Batman',
                    'Year': '1989',
                    'imdbID': 'tt0096895',
                    'Type': 'movie',
                    'Poster': 'https://example.com/poster.jpg',
                },
            ],
            'totalResults': '1',
        }
        results = self.repository.get_movies_from_omdb_search('batman')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, 'Batman')
        self.assertEqual(results[0].imdb_id, 'tt0096895')
        self.assertEqual(results[0].year, '1989')
        self.assertEqual(results[0].type, 'movie')

    @patch('movie.repositories.requests.get')
    def test_get_movies_from_omdb_search_returns_empty_on_error_response(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'Response': 'False', 'Error': 'Movie not found!'}
        results = self.repository.get_movies_from_omdb_search('xyznonexistent')
        self.assertEqual(results, [])

    def test_get_movies_from_db_search_returns_imdb_movies_from_db(self):
        Movie.objects.create(
            title='The Dark Knight',
            imdb_id='tt0468569',
            year='2008',
            type='movie',
            poster='https://example.com/dk.jpg',
        )
        Movie.objects.create(
            title='Dark City',
            imdb_id='tt0118929',
            year='1998',
            type='movie',
            poster='',
        )
        results = self.repository.get_movies_from_db_search('Dark')
        self.assertEqual(len(results), 2)
        titles = {m.title for m in results}
        self.assertIn('The Dark Knight', titles)
        self.assertIn('Dark City', titles)
        for m in results:
            self.assertIsInstance(m, ImdbMovie)
            self.assertTrue(m.imdb_id.startswith('tt'))


class MovieServiceTests(TestCase):
    def test_service_delegates_to_repository(self):
        service = MovieService()
        with patch.dict('django.conf.settings.__dict__', {'MOVIE_SEARCH_PROVIDER': 'imdb'}, clear=False):
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

    @patch.dict('django.conf.settings.__dict__', {'MOVIE_SEARCH_PROVIDER': 'omdb'}, clear=False)
    @patch.object(MovieRepository, 'get_movies_from_omdb_search', return_value=[ImdbMovie('Batman', 'tt0096895', '', '1989', 'movie')])
    def test_get_movies_from_imdb_uses_omdb_when_provider_omdb(self, mock_omdb_search):
        service = MovieService()
        result = service.get_movies_from_imdb('batman')
        mock_omdb_search.assert_called_once_with('batman')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, 'Batman')

    @patch.dict('django.conf.settings.__dict__', {'MOVIE_SEARCH_PROVIDER': 'imdb'}, clear=False)
    @patch.object(MovieRepository, 'get_movies_from_imdb', return_value=[ImdbMovie('Batman', 'tt0096895', '', '1989', 'movie')])
    def test_get_movies_from_imdb_uses_imdb_when_provider_imdb(self, mock_imdb):
        service = MovieService()
        result = service.get_movies_from_imdb('batman')
        mock_imdb.assert_called_once_with('batman')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, 'Batman')

    @patch.dict('django.conf.settings.__dict__', {'MOVIE_SEARCH_PROVIDER': 'omdb'}, clear=False)
    @patch.object(MovieRepository, 'get_movies_from_omdb_search', side_effect=Exception('Network error'))
    @patch.object(MovieRepository, 'get_movies_from_db_search', return_value=[ImdbMovie('Dark Knight', 'tt0468569', '', '2008', 'movie')])
    def test_get_movies_from_imdb_falls_back_to_db_on_provider_error(self, mock_db_search, mock_omdb_search):
        service = MovieService()
        result = service.get_movies_from_imdb('batman')
        mock_omdb_search.assert_called_once_with('batman')
        mock_db_search.assert_called_once_with('batman')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, 'Dark Knight')


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


class TopMoviesServiceTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='top@test.test', password='validpass')
        self.service = TopMoviesService()

    @patch('movie.services.TopMoviesFindMovieAiClient.find_movies')
    @patch('movie.services.MovieRepository.search_movies_in_omdb')
    def test_top_movies_cached_weekly(self, mock_search, mock_find_movies):
        mock_find_movies.return_value = [AiMovie('Hit One'), AiMovie('Hit Two')]

        def fake_search(titles: list[str], initiator_id: int):
            results = []
            for idx, title in enumerate(titles, start=1):
                movie, _ = Movie.objects.get_or_create(title=title, imdb_id=f'ttTop{idx:07d}')
                results.append(OmdbMovie(title=movie.title, imdb_id=movie.imdb_id, id=movie.id))
            return results

        mock_search.side_effect = fake_search

        first_batch = self.service.get_top_movies(user_id=self.user.id)

        self.assertEqual(len(first_batch), 2)
        mock_find_movies.assert_called_once()
        self.assertEqual(TopMovie.objects.count(), 2)

        mock_find_movies.reset_mock()

        second_batch = self.service.get_top_movies(user_id=self.user.id)

        self.assertEqual(len(second_batch), 2)
        mock_find_movies.assert_not_called()

        TopMovie.objects.update(generated_at=timezone.now() - timedelta(days=8))

        refreshed_batch = self.service.get_top_movies(user_id=self.user.id)

        self.assertEqual(len(refreshed_batch), 2)
        mock_find_movies.assert_called_once()

    @patch('movie.services.TopMoviesFindMovieAiClient.find_movies', return_value=[])
    @patch('movie.services.MovieRepository.search_movies_in_omdb', return_value=[])
    def test_top_movies_fallback_to_popular(self, _mock_search, _mock_find_movies):
        liker_one = get_user_model().objects.create_user(email='liker1@test.test', password='pass12345')
        liker_two = get_user_model().objects.create_user(email='liker2@test.test', password='pass12345')

        popular_one = Movie.objects.create(title='Popular One', imdb_id='ttpop0001')
        popular_two = Movie.objects.create(title='Popular Two', imdb_id='ttpop0002')

        LikeMovie.objects.create(user=liker_one, movie=popular_one)
        LikeMovie.objects.create(user=liker_two, movie=popular_one)
        LikeMovie.objects.create(user=liker_one, movie=popular_two)

        results = self.service.get_top_movies(user_id=self.user.id)

        returned_titles = [movie.title for movie in results]
        self.assertIn('Popular One', returned_titles)
        self.assertIn('Popular Two', returned_titles)
        self.assertEqual(TopMovie.objects.count(), len(returned_titles))

    @patch.object(TopMoviesService, '_refresh_top_movies', return_value=[])
    def test_get_top_movies_refreshes_when_cache_empty_and_recent(self, mock_refresh):
        with patch.object(self.service.top_movies_repository, 'get_latest_generated_at', return_value=timezone.now()):
            with patch.object(self.service, '_should_refresh', return_value=False):
                self.service.get_top_movies(user_id=None)

        mock_refresh.assert_called_once_with(None)

    @patch.object(TopMoviesService, '_refresh_top_movies', return_value=['refreshed'])
    def test_force_refresh_delegates(self, mock_refresh):
        result = self.service.force_refresh()

        self.assertEqual(result, ['refreshed'])
        mock_refresh.assert_called_once_with(None)


class TopMoviesRepositoryTests(TestCase):
    def setUp(self):
        self.repository = TopMoviesRepository()
        self.user = get_user_model().objects.create_user(email='toprepo@test.test', password='strongpass')

    def test_replace_top_movies_deduplicates_and_orders(self):
        first = Movie.objects.create(title='First', imdb_id='tttoprep1')
        second = Movie.objects.create(title='Second', imdb_id='tttoprep2')

        generated_at = self.repository.replace_top_movies([first.id, first.id, second.id])

        top_entries = list(TopMovie.objects.order_by('position'))
        self.assertEqual([entry.movie_id for entry in top_entries], [first.id, second.id])
        self.assertEqual(top_entries[0].generated_at.date(), generated_at.date())

    def test_get_top_movies_handles_missing_entries(self):
        self.assertEqual(self.repository.get_top_movies(user_id=None), [])

    def test_get_top_movies_returns_empty_when_no_ids(self):
        with patch.object(self.repository, 'get_latest_generated_at', return_value=timezone.now()):
            with patch('movie.repositories.TopMovie.objects.filter') as mock_filter:
                mock_filter.return_value.order_by.return_value.values_list.return_value = []
                self.assertEqual(self.repository.get_top_movies(user_id=None), [])

    def test_top_movie_str(self):
        movie = Movie.objects.create(title='Stringed', imdb_id='tttoprep4')
        entry = TopMovie.objects.create(movie=movie, position=0)

        self.assertIn('Stringed', str(entry))
