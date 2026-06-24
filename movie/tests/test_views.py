import json
import random
import time
from datetime import timedelta
from types import SimpleNamespace
from typing import List
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import SimpleTestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from movie.dataclasses import AiMovie, ImdbMovie, MovieRecommendation, OmdbMovie
from movie.dataclasses import Genre as GenreDTO
from movie.errors import AddLikeError, AiSearchLimitError
from movie.models import Genre, LikeMovie, Movie, Rating, RecommendedMovie, WatchedMovie, WatchLaterMovie
from movie.views import AI_STREAM_RESOLVE_MAX_WORKERS, MoviesAiSearchStreamView, _stream_resolved_ai_movies


def _issue_jwt(client, user):
    refresh = RefreshToken.for_user(user)
    client.credentials(
        HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}',
        HTTP_USER_AGENT=f'test-agent{random.randint(0, 1000)}',
        HTTP_X_FORWARDED_FOR=f'127.0.0.{random.randint(1, 254)}',
    )


class AiSearchStreamResolveTests(SimpleTestCase):
    def _stream_view_events(self, fake_service, expression='anything'):
        request = APIRequestFactory().post(
            '/movies/ai/search/stream/',
            {'expression': expression},
            format='json',
            HTTP_ACCEPT='application/x-ndjson',
        )
        force_authenticate(request, user=SimpleNamespace(id=1, is_authenticated=True))

        with (
            patch('movie.views._consume_ai_search_quota') as mock_consume_quota,
            patch('movie.views.MovieService', return_value=fake_service),
            patch.object(MoviesAiSearchStreamView, 'throttle_classes', []),
        ):
            response = MoviesAiSearchStreamView.as_view()(request)
            events = [json.loads(chunk.decode('utf-8') if isinstance(chunk, bytes) else chunk) for chunk in response.streaming_content]
        return response, events, mock_consume_quota

    def test_stream_resolve_default_concurrency_is_two(self):
        self.assertEqual(AI_STREAM_RESOLVE_MAX_WORKERS, 2)

    def test_streamed_titles_are_resolved_concurrently(self):
        class FakeMovieService:
            def stream_movies_from_ai(self, expression):
                yield AiMovie(title='Slow', match_score=90)
                yield AiMovie(title='Fast', match_score=95)

            def resolve_ai_movie(self, ai_movie, initiator_id):
                if ai_movie.title == 'Slow':
                    time.sleep(0.05)
                return OmdbMovie(title=ai_movie.title, imdb_id=f'tt{ai_movie.title.lower()}')

        results = list(
            _stream_resolved_ai_movies(
                FakeMovieService(),
                'anything',
                initiator_id=1,
                max_workers=2,
                poll_interval_seconds=0.001,
            )
        )

        self.assertEqual([movie.title for _, _, movie in results], ['Fast', 'Slow'])

    def test_streamed_title_producer_errors_are_propagated(self):
        class FakeMovieService:
            def stream_movies_from_ai(self, expression):
                raise RuntimeError('ai stream failed')
                yield

            def resolve_ai_movie(self, ai_movie, initiator_id):
                return OmdbMovie(title=ai_movie.title)

        with self.assertRaises(RuntimeError) as exc:
            list(
                _stream_resolved_ai_movies(
                    FakeMovieService(),
                    'anything',
                    initiator_id=1,
                    max_workers=2,
                    poll_interval_seconds=0.001,
                )
            )

        self.assertIn('ai stream failed', str(exc.exception))

    def test_streamed_title_resolve_errors_do_not_stop_other_results(self):
        class FakeMovieService:
            def stream_movies_from_ai(self, expression):
                yield AiMovie(title='Broken', match_score=10)
                yield AiMovie(title='Good', match_score=90)

            def resolve_ai_movie(self, ai_movie, initiator_id):
                if ai_movie.title == 'Broken':
                    raise RuntimeError('resolve failed')
                return OmdbMovie(title=ai_movie.title, imdb_id='ttgood')

        results = list(
            _stream_resolved_ai_movies(
                FakeMovieService(),
                'anything',
                initiator_id=1,
                max_workers=2,
                poll_interval_seconds=0.001,
            )
        )

        by_title = {ai_movie.title: movie for _, ai_movie, movie in results}
        self.assertIsNone(by_title['Broken'])
        self.assertEqual(by_title['Good'].title, 'Good')

    def test_ai_search_stream_view_yields_movie_events_from_streamed_titles(self):
        class FakeMovieService:
            def stream_movies_from_ai(self, expression):
                yield AiMovie(title='Pom Poko', year='1994', match_score=92)
                yield AiMovie(title='The Cat Returns', year='2002', match_score=90)

            def resolve_ai_movie(self, ai_movie, initiator_id):
                movies = {
                    'Pom Poko': OmdbMovie(title='Pom Poko', imdb_id='tt0110008', id=1),
                    'The Cat Returns': OmdbMovie(title='The Cat Returns', imdb_id='tt0347618', id=2),
                }
                movie = movies[ai_movie.title]
                movie.match_score = ai_movie.match_score
                return movie

        response, events, mock_consume_quota = self._stream_view_events(FakeMovieService(), 'anime like shrek')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([event['event'] for event in events], ['movie', 'movie', 'done'])
        self.assertEqual([event['data']['title'] for event in events[:2]], ['Pom Poko', 'The Cat Returns'])
        self.assertEqual(events[-1]['requested'], 2)
        self.assertEqual(events[-1]['resolved'], 2)
        mock_consume_quota.assert_called_once()

    def test_ai_search_stream_view_skips_duplicate_resolved_imdb_ids(self):
        class FakeMovieService:
            def stream_movies_from_ai(self, expression):
                yield AiMovie(title='First', match_score=80)
                yield AiMovie(title='Duplicate', match_score=70)

            def resolve_ai_movie(self, ai_movie, initiator_id):
                movie = OmdbMovie(title=ai_movie.title, imdb_id='ttsame', id=1)
                movie.match_score = ai_movie.match_score
                return movie

        _, events, _ = self._stream_view_events(FakeMovieService())

        self.assertEqual([event['event'] for event in events], ['movie', 'done'])
        self.assertEqual(events[0]['data']['title'], 'First')
        self.assertEqual(events[-1]['requested'], 2)
        self.assertEqual(events[-1]['resolved'], 1)

    def test_ai_search_stream_view_yields_error_event_when_ai_stream_fails(self):
        class FakeMovieService:
            def stream_movies_from_ai(self, expression):
                raise RuntimeError('ai stream failed')
                yield

            def resolve_ai_movie(self, ai_movie, initiator_id):
                return OmdbMovie(title=ai_movie.title)

        response, events, _ = self._stream_view_events(FakeMovieService())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(events, [{'event': 'error', 'detail': 'ai stream failed'}])

    def test_ai_search_stream_view_uses_fallback_when_no_streamed_title_resolves(self):
        class FakeMovieService:
            def stream_movies_from_ai(self, expression):
                yield AiMovie(title='Unknown Anime', match_score=87)

            def resolve_ai_movie(self, ai_movie, initiator_id):
                return None

            def get_movies_from_imdb(self, query):
                return [ImdbMovie(title='Fallback Movie', imdb_id='ttfallback', poster='', year='2000', type='movie')]

            def search_movies_in_omdb_from_imdb_list(self, imdb_list, initiator_id):
                return [OmdbMovie(title='Fallback Movie', imdb_id='ttfallback', id=3)]

        response, events, _ = self._stream_view_events(FakeMovieService())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([event['event'] for event in events], ['movie', 'done'])
        self.assertEqual(events[0]['data']['title'], 'Fallback Movie')
        self.assertEqual(events[0]['data']['match_score'], 87)
        self.assertEqual(events[-1]['requested'], 1)
        self.assertEqual(events[-1]['resolved'], 1)

    def test_ai_search_stream_view_tries_next_fallback_query_and_skips_duplicates(self):
        class FakeMovieService:
            def __init__(self):
                self.queries = []

            def stream_movies_from_ai(self, expression):
                yield AiMovie(title='Unknown Anime', match_score=87)

            def resolve_ai_movie(self, ai_movie, initiator_id):
                return None

            def get_movies_from_imdb(self, query):
                self.queries.append(query)
                if query == 'Unknown Anime':
                    return []
                return [ImdbMovie(title='Fallback Movie', imdb_id='ttfallback', poster='', year='2000', type='movie')]

            def search_movies_in_omdb_from_imdb_list(self, imdb_list, initiator_id):
                first = OmdbMovie(title='Fallback Movie', imdb_id='ttfallback', id=3)
                second = OmdbMovie(title='Fallback Duplicate', imdb_id='ttfallback', id=4)
                return [first, second]

        fake_service = FakeMovieService()
        response, events, _ = self._stream_view_events(fake_service, 'original query')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(fake_service.queries, ['Unknown Anime', 'original query'])
        self.assertEqual([event['event'] for event in events], ['movie', 'done'])
        self.assertEqual(events[0]['data']['title'], 'Fallback Movie')
        self.assertEqual(events[-1]['resolved'], 1)

    def test_ai_search_stream_view_ignores_blank_fallback_queries(self):
        class FakeMovieService:
            def __init__(self):
                self.queries = []

            def stream_movies_from_ai(self, expression):
                yield AiMovie(title='', match_score=0)

            def resolve_ai_movie(self, ai_movie, initiator_id):
                return None

            def get_movies_from_imdb(self, query):
                self.queries.append(query)
                return []

        fake_service = FakeMovieService()
        response, events, _ = self._stream_view_events(fake_service, 'original query')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(fake_service.queries, ['original query'])
        self.assertEqual(events, [{'event': 'done', 'requested': 1, 'resolved': 0}])

    def test_ai_search_stream_view_returns_quota_error_response(self):
        request = APIRequestFactory().post(
            '/movies/ai/search/stream/',
            {'expression': 'anime like shrek'},
            format='json',
            HTTP_ACCEPT='application/x-ndjson',
        )
        force_authenticate(request, user=SimpleNamespace(id=1, is_authenticated=True))

        with (
            patch('movie.views._consume_ai_search_quota', side_effect=AiSearchLimitError),
            patch.object(MoviesAiSearchStreamView, 'throttle_classes', []),
        ):
            response = MoviesAiSearchStreamView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)


class FinderTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(title='Test Movie', imdb_id='tt000001', imdb_rating='7.5')

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email='neo@matrix.test', password='thereisnospoon')
        _issue_jwt(self.client, self.user)

    def test_get_movie(self):
        response = self.client.get(reverse('movie', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.movie.title)

    def test_like_movie(self):
        response = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(LikeMovie.objects.filter(user=self.user, movie=self.movie).exists())

    def test_like_movie_error(self):
        LikeMovie.objects.create(user=self.user, movie=self.movie)

        response = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'].code, AddLikeError.default_code)
        self.assertEqual(response.data['detail'], AddLikeError.default_detail)

    def test_unlike_movie(self):
        LikeMovie.objects.create(user=self.user, movie=self.movie)

        response = self.client.post(reverse('movie_unlike', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(LikeMovie.objects.filter(user=self.user, movie=self.movie).exists())

    @patch('movie.views.MovieService.search_movies_in_omdb_from_imdb_list')
    @patch('movie.views.MovieService.get_movies_from_imdb')
    def test_find_movie(self, mock_imdb, mock_search_from_list):
        imdb_list = [
            ImdbMovie(
                title='Shrek',
                imdb_id='tt0126029',
                poster='http://poster.url',
                year='2001',
                type='movie',
            ),
        ]
        mock_imdb.return_value = imdb_list
        mock_search_from_list.return_value = [
            OmdbMovie(title='Shrek', imdb_id='tt0126029', genres=[GenreDTO(name='Animation')], id=self.movie.id),
        ]

        response = self.client.post(
            reverse('movies_search'),
            data={'expression': 'Shrek'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Shrek')
        self.assertEqual(response.data[0]['id'], self.movie.id)
        mock_imdb.assert_called_once_with('Shrek')
        mock_search_from_list.assert_called_once_with(imdb_list, self.user.id)

    def test_create_watch_later(self):
        response = self.client.post(reverse('watch_later_create'), data={'movie': self.movie.id})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(WatchLaterMovie.objects.filter(user=self.user, movie=self.movie).exists())

    def test_delete_watch_later(self):
        WatchLaterMovie.objects.create(user=self.user, movie=self.movie)

        response = self.client.delete(reverse('watch_later_destroy', kwargs={'pk': self.movie.id}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(WatchLaterMovie.objects.filter(user=self.user, movie=self.movie).exists())

    def test_get_watch_later(self):
        WatchLaterMovie.objects.create(user=self.user, movie=self.movie)

        response = self.client.get(reverse('watch_later_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['id'], self.movie.id)
        self.assertTrue(response.data['results'][0]['is_watch_later'])
        self.assertFalse(response.data['results'][0]['is_watched'])

    def test_mark_and_unmark_watched(self):
        response = self.client.post(reverse('movie_watched', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(WatchedMovie.objects.filter(user=self.user, movie=self.movie).exists())

        detail = self.client.get(reverse('movie', kwargs={'id': self.movie.id}))
        self.assertTrue(detail.data['is_watched'])

        response = self.client.post(reverse('movie_unwatched', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(WatchedMovie.objects.filter(user=self.user, movie=self.movie).exists())

    def test_watch_later_filter_by_watched(self):
        watched_movie = Movie.objects.create(title='Watched', imdb_id='tt-watched-1')
        unwatched_movie = Movie.objects.create(title='Unwatched', imdb_id='tt-unwatched-1')
        WatchLaterMovie.objects.create(user=self.user, movie=watched_movie)
        WatchLaterMovie.objects.create(user=self.user, movie=unwatched_movie)
        WatchedMovie.objects.create(user=self.user, movie=watched_movie)

        watched_only = self.client.get(reverse('watch_later_list'), {'is_watched': 'true'})
        self.assertEqual(watched_only.status_code, status.HTTP_200_OK)
        self.assertEqual({item['id'] for item in watched_only.data['results']}, {watched_movie.id})

        unwatched_only = self.client.get(reverse('watch_later_list'), {'is_watched': 'false'})
        self.assertEqual(unwatched_only.status_code, status.HTTP_200_OK)
        self.assertEqual({item['id'] for item in unwatched_only.data['results']}, {unwatched_movie.id})

    def test_watch_later_default_order_puts_watched_last(self):
        unwatched_movie = Movie.objects.create(title='Unwatched Order', imdb_id='tt-unwatched-order')
        watched_movie = Movie.objects.create(title='Watched Order', imdb_id='tt-watched-order')
        unwatched_entry = WatchLaterMovie.objects.create(user=self.user, movie=unwatched_movie)
        watched_entry = WatchLaterMovie.objects.create(user=self.user, movie=watched_movie)
        WatchedMovie.objects.create(user=self.user, movie=watched_movie)

        earlier_time = timezone.now() - timedelta(days=2)
        WatchLaterMovie.objects.filter(pk=unwatched_entry.pk).update(created_at=earlier_time)
        WatchLaterMovie.objects.filter(pk=watched_entry.pk).update(created_at=timezone.now())

        response = self.client.get(reverse('watch_later_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            [item['id'] for item in response.data['results']],
            [unwatched_movie.id, watched_movie.id],
        )

    def test_watch_later_ordering_by_added_at(self):
        older_movie = Movie.objects.create(title='Older Movie', imdb_id='tt000002')
        newer_movie = Movie.objects.create(title='Newer Movie', imdb_id='tt000003')

        older_entry = WatchLaterMovie.objects.create(user=self.user, movie=older_movie)
        WatchLaterMovie.objects.create(user=self.user, movie=newer_movie)

        earlier_time = timezone.now() - timedelta(days=1)
        WatchLaterMovie.objects.filter(pk=older_entry.pk).update(created_at=earlier_time)

        response = self.client.get(reverse('watch_later_list'), {'ordering': 'added_at'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        ascending_ids = [item['id'] for item in response.data['results']]
        self.assertEqual(ascending_ids, [older_movie.id, newer_movie.id])

        response_desc = self.client.get(reverse('watch_later_list'), {'ordering': '-added_at'})
        self.assertEqual(response_desc.status_code, status.HTTP_200_OK)
        descending_ids = [item['id'] for item in response_desc.data['results']]
        self.assertEqual(descending_ids, [newer_movie.id, older_movie.id])

    def test_watch_later_statistics(self):
        genres = [Genre.objects.create(name=f'Genre {idx}') for idx in range(6)]
        rating_values = ['9.1', '8.5', '7.5', '6.5', '5.5', '4.5']

        for idx, value in enumerate(rating_values):
            movie = Movie.objects.create(title=f'Movie {idx}', imdb_id=f'tt{1000 + idx}', year=str(2000 + idx))
            movie.genres.add(genres[idx])
            Rating.objects.create(movie=movie, source='imdb', value=value)
            WatchLaterMovie.objects.create(user=self.user, movie=movie)

        response = self.client.get(reverse('watch_later_statistics'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        ratings = response.data['ratings']
        self.assertEqual(ratings['ratings_9_plus'], 1)
        self.assertEqual(ratings['ratings_8_to_9'], 1)
        self.assertEqual(ratings['ratings_7_to_8'], 1)
        self.assertEqual(ratings['ratings_6_to_7'], 1)
        self.assertEqual(ratings['ratings_5_to_6'], 1)
        self.assertEqual(ratings['ratings_below_5'], 1)
        self.assertEqual(response.data['genres'][0]['count'], 1)

    def test_watch_later_statistics_excludes_null_genres(self):
        movie_with_genre = Movie.objects.create(title='Has Genre', imdb_id='tt9001', year='2020')
        movie_with_genre.genres.add(Genre.objects.create(name='Drama'))
        movie_no_genre = Movie.objects.create(title='No Genre', imdb_id='tt9002', year='2021')
        WatchLaterMovie.objects.create(user=self.user, movie=movie_with_genre)
        WatchLaterMovie.objects.create(user=self.user, movie=movie_no_genre)

        response = self.client.get(reverse('watch_later_statistics'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        genre_names = [g['genre'] for g in response.data['genres']]
        self.assertIn('Drama', genre_names)
        self.assertNotIn(None, genre_names)

    def test_watch_later_filter_by_rating(self):
        high_rated = Movie.objects.create(title='Highly Rated', imdb_id='tt010001', imdb_rating='9.0')
        low_rated = Movie.objects.create(title='Low Rated', imdb_id='tt010002', imdb_rating='5.0')
        WatchLaterMovie.objects.create(user=self.user, movie=high_rated)
        WatchLaterMovie.objects.create(user=self.user, movie=low_rated)

        response = self.client.get(reverse('watch_later_list'), {'rating_min': 8})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, ['Highly Rated'])

    def test_watch_later_search(self):
        mystery_movie = Movie.objects.create(title='Mystery Story', imdb_id='tt020001', imdb_rating='7.0')
        action_movie = Movie.objects.create(title='Action Blast', imdb_id='tt020002', imdb_rating='8.0')
        WatchLaterMovie.objects.create(user=self.user, movie=mystery_movie)
        WatchLaterMovie.objects.create(user=self.user, movie=action_movie)

        response = self.client.get(reverse('watch_later_list'), {'search': 'Mystery'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, ['Mystery Story'])


class FindMovieAiTests(APITestCase):
    def setUp(self):
        cache.clear()
        self.user = get_user_model().objects.create_user(email='trinity@matrix.test', password='followthewhiterabbit')
        _issue_jwt(self.client, self.user)

    def _guest_headers(self):
        return {
            'HTTP_USER_AGENT': 'guest-ai-search-agent',
            'HTTP_X_FORWARDED_FOR': '203.0.113.77, 10.0.0.1',
        }

    @patch('movie.views.MovieService.resolve_ai_search')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_find_movie_ai(self, mock_ai, mock_resolve):
        mock_ai.return_value = [AiMovie(title='Shrek'), AiMovie(title='Shrek 2')]

        def fake_resolve(ai_movies, initiator_id, expression=''):
            results = []
            for idx, ai_movie in enumerate(ai_movies, start=1):
                title = ai_movie.title
                imdb_id = f'tt{idx:07d}'
                movie, _ = Movie.objects.get_or_create(title=title, imdb_id=imdb_id)
                results.append(
                    OmdbMovie(
                        title=movie.title,
                        imdb_id=movie.imdb_id,
                        plot=f'Plot for {title}',
                        genres=[GenreDTO(name='Animation')],
                        id=movie.id,
                        match_score=ai_movie.match_score,
                    )
                )
            return results

        mock_resolve.side_effect = fake_resolve

        response = self.client.post(
            reverse('movies_ai_search'),
            data={'expression': 'family animation about ogres'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertTrue(Movie.objects.filter(title='Shrek').exists())
        self.assertEqual(response.data[0]['genres'][0]['name'], 'Animation')
        self.assertEqual(response.data[0]['plot'], 'Plot for Shrek')
        self.assertIsNotNone(response.data[0]['id'])

    def test_prompt_max_length(self):
        max_length = 255
        payload = {'expression': 'A' * (max_length + 1)}

        response = self.client.post(reverse('movies_ai_search'), data=payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('expression', response.data)
        self.assertIn('Ensure this field has no more than', response.data['expression'][0])

    @patch('movie.views.MovieService.resolve_ai_search')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_guest_first_ai_search_request_is_allowed(self, mock_ai, mock_resolve):
        self.client.credentials()
        mock_ai.return_value = [AiMovie(title='Shrek')]
        mock_resolve.return_value = []

        response = self.client.post(
            reverse('movies_ai_search'),
            data={'expression': 'guest query'},
            format='json',
            **self._guest_headers(),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_ai.assert_called_once_with('guest query')
        mock_resolve.assert_called_once_with(mock_ai.return_value, None, 'guest query')

    @patch('movie.views.MovieService.resolve_ai_search')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_guest_second_ai_search_request_is_blocked_before_ai_provider(self, mock_ai, mock_resolve):
        self.client.credentials()
        mock_ai.return_value = [AiMovie(title='Shrek')]
        mock_resolve.return_value = []
        payload = {'expression': 'guest query'}
        headers = self._guest_headers()

        first_response = self.client.post(reverse('movies_ai_search'), data=payload, format='json', **headers)
        second_response = self.client.post(reverse('movies_ai_search'), data=payload, format='json', **headers)

        self.assertEqual(first_response.status_code, status.HTTP_200_OK)
        self.assertEqual(second_response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
        self.assertEqual(second_response.data['detail'].code, AiSearchLimitError.default_code)
        self.assertEqual(second_response.data['detail'], AiSearchLimitError.default_detail)
        mock_ai.assert_called_once()
        mock_resolve.assert_called_once()

    @patch('movie.views.MovieService.resolve_ai_search')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_authenticated_ai_search_does_not_use_guest_limit(self, mock_ai, mock_resolve):
        mock_ai.return_value = []
        mock_resolve.return_value = []
        payload = {'expression': 'authenticated query'}

        first_response = self.client.post(reverse('movies_ai_search'), data=payload, format='json')
        second_response = self.client.post(reverse('movies_ai_search'), data=payload, format='json')

        self.assertEqual(first_response.status_code, status.HTTP_200_OK)
        self.assertEqual(second_response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.ai_search_count, 2)
        self.assertEqual(mock_ai.call_count, 2)
        self.assertEqual(mock_resolve.call_count, 2)

    @patch('movie.views.MovieService.resolve_ai_search')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_ai_search_limit_enforced(self, mock_ai, mock_resolve):
        mock_ai.return_value = []
        mock_resolve.return_value = []
        tier_limit = self.user.account_tier.daily_ai_search_limit
        self.user.ai_search_count = tier_limit
        self.user.ai_search_count_reset_at = timezone.now().date()
        self.user.save(update_fields=['ai_search_count', 'ai_search_count_reset_at'])

        response = self.client.post(
            reverse('movies_ai_search'),
            data={'expression': 'limit test'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
        mock_ai.assert_not_called()
        mock_resolve.assert_not_called()

    @patch('movie.views.MovieService.resolve_ai_search')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_ai_search_fallback_when_omdb_exact_match_fails(self, mock_ai, mock_resolve):
        mock_ai.return_value = [AiMovie(title='A Knight of the Seven Kingdoms', match_score=90)]
        movie = Movie.objects.create(
            title='Game of Thrones',
            imdb_id='tt0944947',
            year='2011',
            imdb_rating='9.2',
            plot='Plot',
        )
        mock_resolve.return_value = [
            OmdbMovie(
                title=movie.title,
                imdb_id=movie.imdb_id,
                id=movie.id,
                plot=movie.plot or '',
                genres=[GenreDTO(name='Drama')],
                directors=[],
                writers=[],
                actors=[],
                ratings=[],
                languages=[],
                countries=[],
                match_score=90,
            )
        ]

        response = self.client.post(
            reverse('movies_ai_search'),
            data={'expression': 'Лицар семи королівств'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Game of Thrones')
        mock_resolve.assert_called_once()

    @patch('movie.views.MovieService.resolve_ai_search')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_ai_search_limit_resets_daily(self, mock_ai, mock_resolve):
        mock_ai.return_value = []
        mock_resolve.return_value = []
        yesterday = timezone.now().date() - timedelta(days=1)
        tier_limit = self.user.account_tier.daily_ai_search_limit
        self.user.ai_search_count = tier_limit
        self.user.ai_search_count_reset_at = yesterday
        self.user.save(update_fields=['ai_search_count', 'ai_search_count_reset_at'])

        response = self.client.post(
            reverse('movies_ai_search'),
            data={'expression': 'reset me'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        mock_ai.assert_called_once()
        mock_resolve.assert_called_once()

    @patch('movie.views.logging.getLogger')
    @patch('movie.views.MovieService.resolve_ai_search')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_ai_search_logs_and_reraises_on_service_error(self, mock_ai, mock_resolve, mock_get_logger):
        mock_ai.side_effect = RuntimeError('AI service down')
        mock_resolve.return_value = []
        mock_logger = mock_get_logger.return_value

        response = self.client.post(
            reverse('movies_ai_search'),
            data={'expression': 'something'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        mock_logger.exception.assert_called_once()
        pos_args = mock_logger.exception.call_args[0]
        self.assertIn('movies/ai/search failed', pos_args[0])
        self.assertIn('AI service down', str(pos_args[1]))

    @patch('movie.views.MovieService.resolve_ai_movie')
    @patch('movie.views.MovieService.get_movies_from_ai')
    @patch('movie.views.MovieService.stream_movies_from_ai')
    def test_ai_search_stream_resolves_openai_titles_as_they_stream(self, mock_stream_ai, mock_get_movies_from_ai, mock_resolve_movie):
        mock_stream_ai.return_value = iter(
            [
                AiMovie(title='Pom Poko', year='1994', match_score=92),
                AiMovie(title='The Cat Returns', year='2002', match_score=90),
            ]
        )

        def fake_resolve(ai_movie, initiator_id):
            movie, _ = Movie.objects.get_or_create(title=ai_movie.title, imdb_id=f'tt{len(ai_movie.title):07d}')
            return OmdbMovie(
                title=movie.title,
                imdb_id=movie.imdb_id,
                genres=[GenreDTO(name='Animation')],
                id=movie.id,
            )

        mock_resolve_movie.side_effect = fake_resolve

        response = self.client.post(
            reverse('movies_ai_search_stream'),
            data={'expression': 'anime like shrek'},
            format='json',
            HTTP_ACCEPT='application/x-ndjson',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        events = [json.loads(chunk.decode('utf-8') if isinstance(chunk, bytes) else chunk) for chunk in response.streaming_content]
        movie_events = [event for event in events if event['event'] == 'movie']
        ordered_movie_events = sorted(movie_events, key=lambda event: event['index'])

        self.assertEqual([event['data']['title'] for event in ordered_movie_events], ['Pom Poko', 'The Cat Returns'])
        self.assertEqual(events[-1]['event'], 'done')
        self.assertEqual(events[-1]['requested'], 2)
        self.assertEqual(events[-1]['resolved'], 2)
        mock_stream_ai.assert_called_once_with('anime like shrek')
        mock_get_movies_from_ai.assert_not_called()
        self.assertEqual(mock_resolve_movie.call_count, 2)

    @patch('movie.views.MovieService.resolve_ai_movie')
    @patch('movie.views.MovieService.stream_movies_from_ai')
    def test_guest_ai_search_stream_second_request_is_blocked_before_ai_provider(self, mock_stream_ai, mock_resolve_movie):
        self.client.credentials()
        mock_stream_ai.return_value = iter([AiMovie(title='Pom Poko', year='1994', match_score=92)])
        mock_resolve_movie.return_value = OmdbMovie(title='Pom Poko', imdb_id='tt0110008', genres=[GenreDTO(name='Animation')], id=1)
        payload = {'expression': 'guest stream query'}
        headers = self._guest_headers()

        first_response = self.client.post(
            reverse('movies_ai_search_stream'),
            data=payload,
            format='json',
            HTTP_ACCEPT='application/x-ndjson',
            **headers,
        )
        first_events = [json.loads(chunk.decode('utf-8') if isinstance(chunk, bytes) else chunk) for chunk in first_response.streaming_content]
        second_response = self.client.post(
            reverse('movies_ai_search_stream'),
            data=payload,
            format='json',
            HTTP_ACCEPT='application/x-ndjson',
            **headers,
        )

        self.assertEqual(first_response.status_code, status.HTTP_200_OK)
        self.assertEqual(first_events[-1]['event'], 'done')
        self.assertEqual(second_response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
        self.assertEqual(second_response.data['detail'].code, AiSearchLimitError.default_code)
        mock_stream_ai.assert_called_once_with('guest stream query')
        mock_resolve_movie.assert_called_once()


class FindMovieFiltersTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.genre_comedy = Genre.objects.create(name='Comedy')
        cls.genre_animation = Genre.objects.create(name='Animation')

        cls.shrek = Movie.objects.create(title='Shrek', imdb_id='tt000010', year='2001', imdb_rating='7.2')
        cls.shrek.genres.add(cls.genre_comedy)

        cls.shrek_2 = Movie.objects.create(title='Shrek 2', imdb_id='tt000020', year='2004', imdb_rating='8.6')
        cls.shrek_2.genres.add(cls.genre_animation)

        cls.user = get_user_model().objects.create_user(email='morpheus@matrix.test', password='redpillbluepill')
        LikeMovie.objects.create(user=cls.user, movie=cls.shrek)

    def setUp(self):
        _issue_jwt(self.client, self.user)

    def _get_movies(self, params=None):
        params = params or {}
        return self.client.get(reverse('movies_list'), data=params)

    def test_filter_by_title(self):
        response = self._get_movies({'title': 'Shrek 2'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, ['Shrek 2'])

    def test_filter_by_genre(self):
        response = self._get_movies({'genres': 'Animation'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, ['Shrek 2'])

    def test_filter_by_year(self):
        response = self._get_movies({'year': '2001'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, ['Shrek'])

    def test_filter_by_imdb_id(self):
        response = self._get_movies({'imdb_id': 'tt000010'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, ['Shrek'])

    def test_filter_by_rating_min(self):
        response = self._get_movies({'rating_min': 8})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, ['Shrek 2'])

    def test_filter_by_rating_max(self):
        response = self._get_movies({'rating_max': 7.5})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, ['Shrek'])

    def test_sorting_by_title(self):
        response = self._get_movies({'ordering': 'title'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, sorted(titles))

    def test_sorting_by_year(self):
        response = self._get_movies({'ordering': 'year'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [movie['year'] for movie in response.data['results']]
        self.assertEqual(years, sorted(years))

    def test_sorting_by_imdb_id(self):
        response = self._get_movies({'ordering': 'imdb_id'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        imdb_ids = [movie['imdb_id'] for movie in response.data['results']]
        self.assertEqual(imdb_ids, sorted(imdb_ids))

    def test_sorting_by_imdb_rating(self):
        response = self._get_movies({'ordering': 'imdb_rating'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        ratings = [movie['imdb_rating'] for movie in response.data['results']]
        self.assertEqual(ratings, sorted(ratings))
        response_desc = self._get_movies({'ordering': '-imdb_rating'})
        self.assertEqual(response_desc.status_code, status.HTTP_200_OK)
        ratings_desc = [movie['imdb_rating'] for movie in response_desc.data['results']]
        self.assertEqual(ratings_desc, sorted(ratings_desc, reverse=True))


class MovieModelRepresentationTests(APITestCase):
    def test_movie_str(self):
        movie = Movie.objects.create(title='Representation Test', imdb_id='tt999999')

        self.assertEqual(str(movie), 'Representation Test')

    def test_user_movie_str(self):
        user = get_user_model().objects.create_user(email='repr@test.test', password='thereisnospoon')
        movie = Movie.objects.create(title='String Movie', imdb_id='tt888888')
        like = LikeMovie.objects.create(user=user, movie=movie)

        self.assertEqual(str(like), f'{user} | {movie}')

    def test_recommended_movie_str(self):
        user = get_user_model().objects.create_user(email='rec@test.test', password='thereisnospoon')
        movie = Movie.objects.create(title='Suggested Movie', imdb_id='tt777777')
        recommendation = RecommendedMovie.objects.create(
            user=user,
            movie=movie,
            recommendation_date=timezone.now().date(),
        )

        self.assertEqual(str(recommendation), f'{user} | {movie} | {recommendation.recommendation_date}')


class GenreListViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.genre_comedy = Genre.objects.create(name='Comedy')
        cls.genre_animation = Genre.objects.create(name='Animation')
        cls.genre_fantasy = Genre.objects.create(name='Fantasy')
        cls.genre_horror = Genre.objects.create(name='Horror')

    def test_get_genres(self):
        url = reverse('genre-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_genres = sorted(['Comedy', 'Animation', 'Fantasy', 'Horror'])
        actual_genres = sorted(response.data['genres'])

        self.assertEqual(actual_genres, expected_genres)


class RecommendedMoviesTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='recommend@test.com', password='strongpass')
        _issue_jwt(self.client, self.user)

        self.genre_action = Genre.objects.create(name='Action')
        self.genre_drama = Genre.objects.create(name='Drama')

        self.liked_movie = Movie.objects.create(title='Old Favorite', imdb_id='tt9000001', year='2000')
        self.liked_movie.genres.add(self.genre_action)
        LikeMovie.objects.create(user=self.user, movie=self.liked_movie)

        self.watch_later_movie = Movie.objects.create(title='Pending Watch', imdb_id='tt9000002', year='2005')
        self.watch_later_movie.genres.add(self.genre_drama)
        WatchLaterMovie.objects.create(user=self.user, movie=self.watch_later_movie)

    @patch('movie.services.MovieRepository.search_movies_in_omdb')
    @patch('movie.services.FindMovieAiClient.find_movies')
    def test_recommendations_cached_per_day(self, mock_find_movies, mock_search):
        mock_find_movies.return_value = [AiMovie(title='Recommended One'), AiMovie(title='Recommended Two')]

        def fake_search(titles: List[str], initiator_id: int):
            results = []
            for idx, title in enumerate(titles, start=1):
                movie, _ = Movie.objects.get_or_create(title=title, imdb_id=f'ttrec{idx:07d}')
                results.append(OmdbMovie(title=movie.title, imdb_id=movie.imdb_id, genres=[GenreDTO(name='Action')]))
            return results

        mock_search.side_effect = fake_search

        first_response = self.client.get(reverse('movies_recommendations'))

        self.assertEqual(first_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(first_response.data), 2)
        mock_find_movies.assert_called_once()
        self.assertEqual(RecommendedMovie.objects.filter(user=self.user, recommendation_date=timezone.now().date()).count(), 2)

        mock_find_movies.reset_mock()
        mock_search.reset_mock()

        second_response = self.client.get(reverse('movies_recommendations'))

        self.assertEqual(second_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(second_response.data), 2)
        mock_find_movies.assert_not_called()
        mock_search.assert_not_called()

    @patch('movie.services.MovieRepository.search_movies_in_omdb', return_value=[])
    @patch('movie.services.RecommendationFindMovieAiClient.find_movies')
    def test_recommendations_fallback_when_ai_fails(self, mock_find_movies, _mock_search):
        mock_find_movies.side_effect = Exception('API credit balance too low')
        other_user = get_user_model().objects.create_user(email='other@test.com', password='strongpass')
        popular = Movie.objects.create(title='Popular Fallback', imdb_id='tt8000003', year='2012')
        LikeMovie.objects.create(user=other_user, movie=popular)

        response = self.client.get(reverse('movies_recommendations'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        titles = [item['title'] for item in response.data]
        self.assertIn('Popular Fallback', titles)

    @patch('movie.services.FindMovieAiClient.find_movies')
    def test_recommendations_fallback_to_popular(self, mock_find_movies):
        mock_find_movies.return_value = []

        other_user = get_user_model().objects.create_user(email='other@test.com', password='strongpass')
        second_user = get_user_model().objects.create_user(email='second@test.com', password='strongpass')
        fallback_user = get_user_model().objects.create_user(email='fallback@test.com', password='strongpass')
        _issue_jwt(self.client, fallback_user)
        popular_one = Movie.objects.create(title='Popular One', imdb_id='tt8000001', year='2010')
        popular_two = Movie.objects.create(title='Popular Two', imdb_id='tt8000002', year='2011')
        LikeMovie.objects.create(user=other_user, movie=popular_one)
        LikeMovie.objects.create(user=second_user, movie=popular_one)
        LikeMovie.objects.create(user=other_user, movie=popular_two)

        response = self.client.get(reverse('movies_recommendations'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Popular One')
        mock_find_movies.assert_not_called()
        self.assertEqual(RecommendedMovie.objects.filter(user=fallback_user, recommendation_date=timezone.now().date()).count(), 0)


class TopMoviesViewTests(APITestCase):
    def test_get_top_movies_returns_cached_entries(self):
        top_movies = [
            MovieRecommendation(
                id=1,
                imdb_id='tttop001',
                title='Top One',
                year='2023',
                released_date=None,
                runtime=None,
                plot=None,
                awards=None,
                poster=None,
                metascore=None,
                imdb_rating=None,
                imdb_votes=None,
                type='movie',
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
        ]

        with patch('movie.views.TopMoviesService.get_top_movies', return_value=top_movies) as mock_service:
            response = self.client.get(reverse('movies_top'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Top One')
        self.assertIsNone(mock_service.call_args.args[0])


class MovieTrailerViewTests(APITestCase):
    @patch('movie.views.lookup_trailer_video_id', return_value='abc123xyz')
    def test_returns_video_id(self, _mock_lookup):
        response = self.client.get(
            reverse('movie_trailer'),
            {'title': 'The Matrix', 'year': '1999', 'imdb_id': 'tt0133093'},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['videoId'], 'abc123xyz')

    @patch('movie.views.lookup_trailer_video_id', return_value=None)
    def test_returns_404_when_not_found(self, _mock_lookup):
        response = self.client.get(reverse('movie_trailer'), {'title': 'Unknown Movie'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIsNone(response.data['videoId'])
