import json
from datetime import date, timedelta
from unittest.mock import MagicMock, patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from movie.dataclasses import (
    Actor as ActorDTO,
)
from movie.dataclasses import (
    AiMovie,
    MovieRecommendation,
    OmdbMovie,
    UserActivitySummary,
    UserContext,
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
from movie.services import MovieRecommendationService, MovieService, TopMoviesService


class MovieFilterTests(TestCase):
    def test_rating_filters_ignore_none(self):
        queryset = Movie.objects.all()
        filterset = MovieFilter(data={}, queryset=queryset)

        self.assertIs(filterset.filter_rating_min(queryset, 'rating_min', None), queryset)
        self.assertIs(filterset.filter_rating_max(queryset, 'rating_max', None), queryset)

    def test_filter_title_searches_both_languages(self):
        movie_en = Movie.objects.create(title='English Title', imdb_id='tt0101001')
        movie_ua = Movie.objects.create(title='Placeholder', title_ua='Українська назва', imdb_id='tt0101002')

        queryset = Movie.objects.all()
        filterset = MovieFilter(data={'title': 'українська'}, queryset=queryset)
        results = filterset.qs

        self.assertNotIn(movie_en, results)
        self.assertIn(movie_ua, results)

    def test_filter_title_returns_queryset_when_blank(self):
        queryset = Movie.objects.all()
        returned = MovieFilter.filter_title(queryset, 'title', '')

        self.assertIs(returned, queryset)


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
    def test_search_movies_in_omdb_sets_localized_title_on_new(self, mock_get_movie):
        localized_title = 'Бренд'
        omdb_movie = OmdbMovie(title='Brand', imdb_id='tt010010', title_ua='Old Name')
        mock_get_movie.return_value = omdb_movie
        user = get_user_model().objects.create_user(email='ua@test.test', password='validpass')

        results = self.repository.search_movies_in_omdb([('Brand', localized_title)], initiator_id=user.id)

        created = Movie.objects.get(imdb_id='tt010010')
        self.assertEqual(created.title_ua, localized_title)
        self.assertEqual(results[0].title_ua, localized_title)

    @patch.object(MovieRepository, 'get_movie_from_omdb_by_expression')
    def test_search_movies_in_omdb_sets_missing_localized_title_on_new(self, mock_get_movie):
        localized_title = 'Новий бренд'
        omdb_movie = OmdbMovie(title='BrandNew', imdb_id='tt010011', title_ua=None)
        mock_get_movie.return_value = omdb_movie
        user = get_user_model().objects.create_user(email='ua3@test.test', password='validpass')

        results = self.repository.search_movies_in_omdb([('BrandNew', localized_title)], initiator_id=user.id)

        created = Movie.objects.get(imdb_id='tt010011')
        self.assertEqual(created.title_ua, localized_title)
        self.assertEqual(results[0].title_ua, localized_title)

    def test_search_movies_in_omdb_updates_localized_title_on_existing(self):
        user = get_user_model().objects.create_user(email='ua2@test.test', password='validpass')
        existing = Movie.objects.create(title='Existing', imdb_id='tt010020', title_ua='')

        results = self.repository.search_movies_in_omdb([('Existing', 'Існуючий')], initiator_id=user.id)

        existing.refresh_from_db()
        self.assertEqual(existing.title_ua, 'Існуючий')
        self.assertEqual(results[0].title_ua, 'Існуючий')


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


class MovieRecommendationServiceTests(TestCase):
    def test_recommendations_skip_empty_and_deduplicate_titles(self):
        ai_movies = [
            AiMovie(title='One'),
            AiMovie(title='One', title_ua='Один'),
            AiMovie(title='One', title_ua='Один'),
            AiMovie(title='', title_ua='Без назви'),
        ]

        mock_ai_client = MagicMock(find_movies=MagicMock(return_value=ai_movies))
        mock_movie_repo = MagicMock()
        omdb_result = OmdbMovie(title='One', title_ua='Один', imdb_id='tt1', id=1)
        mock_movie_repo.search_movies_in_omdb.return_value = [omdb_result]
        recommended = MovieRecommendation(
            id=1,
            imdb_id='tt1',
            title='One',
            title_ua='Один',
            year=None,
            released_date=None,
            runtime=None,
            plot=None,
            awards=None,
            poster=None,
            metascore=None,
            imdb_rating=None,
            imdb_votes=None,
            type=None,
            total_seasons=None,
            created_at=None,
            genres=[],
            actors=[],
            directors=[],
            writers=[],
            ratings=[],
            languages=[],
            countries=[],
            is_liked=False,
            likes_count=0,
            is_watch_later=False,
            watch_later_count=0,
        )
        mock_rec_repo = MagicMock()
        mock_rec_repo.get_cached_movie_ids.return_value = []
        mock_rec_repo.get_user_activity_summary.return_value = UserActivitySummary(
            top_genres=[],
            top_directors=[],
            top_actors=[],
            liked_titles=[],
            watch_later_titles=[],
            has_movies=True,
        )
        mock_rec_repo.get_movies_by_titles.return_value = [recommended]
        mock_rec_repo.get_popular_movies.return_value = []
        mock_prompt_service = MagicMock(build_prompt=MagicMock(return_value='prompt'))

        service = MovieRecommendationService(
            recommendation_repository=mock_rec_repo,
            movie_repository=mock_movie_repo,
            prompt_service=mock_prompt_service,
            ai_client=mock_ai_client,
        )

        result = service.get_recommended_movies(UserContext(id=1))

        mock_movie_repo.search_movies_in_omdb.assert_called_once_with(['One', ('One', 'Один')], 1)
        mock_rec_repo.get_movies_by_titles.assert_called_once()
        self.assertEqual(len(result), 1)


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
        mock_find_movies.return_value = [AiMovie('Hit One', title_ua='Хіт Один'), AiMovie('Hit Two')]

        def fake_search(titles: list[str], initiator_id: int):
            results = []
            for idx, title_entry in enumerate(titles, start=1):
                if isinstance(title_entry, tuple):
                    title, title_ua = title_entry
                else:
                    title, title_ua = title_entry, None
                movie, _ = Movie.objects.get_or_create(title=title, imdb_id=f'ttTop{idx:07d}')
                results.append(OmdbMovie(title=movie.title, title_ua=title_ua, imdb_id=movie.imdb_id, id=movie.id))
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

    def test_top_movies_deduplicates_ai_titles(self):
        mock_ai = MagicMock(
            find_movies=MagicMock(
                return_value=[AiMovie('One'), AiMovie('One'), AiMovie('One', title_ua='Один'), AiMovie('', title_ua='Без')],
            ),
        )
        mock_movie_repo = MagicMock()
        mock_movie_repo.search_movies_in_omdb.return_value = [OmdbMovie(title='One', title_ua='Один', imdb_id='tt123', id=1)]
        recommended = MovieRecommendation(
            id=1,
            imdb_id='tt123',
            title='One',
            title_ua='Один',
            year=None,
            released_date=None,
            runtime=None,
            plot=None,
            awards=None,
            poster=None,
            metascore=None,
            imdb_rating=None,
            imdb_votes=None,
            type=None,
            total_seasons=None,
            created_at=None,
            genres=[],
            actors=[],
            directors=[],
            writers=[],
            ratings=[],
            languages=[],
            countries=[],
            is_liked=False,
            likes_count=0,
            is_watch_later=False,
            watch_later_count=0,
        )
        mock_top_repo = MagicMock()
        mock_top_repo.get_latest_generated_at.return_value = None
        mock_top_repo.get_top_movies.side_effect = [[], [recommended]]
        mock_top_repo.replace_top_movies = MagicMock()
        mock_rec_repo = MagicMock(get_popular_movies=MagicMock(return_value=[]))

        service = TopMoviesService(
            top_movies_repository=mock_top_repo,
            movie_repository=mock_movie_repo,
            recommendation_repository=mock_rec_repo,
            ai_client=mock_ai,
        )

        service.get_top_movies(user_id=None)

        mock_movie_repo.search_movies_in_omdb.assert_called_once_with(['One', ('One', 'Один')], initiator_id=0)

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
