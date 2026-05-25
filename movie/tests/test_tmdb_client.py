from unittest.mock import patch

from django.test import SimpleTestCase, override_settings

from movie.tmdb_client import (
    _map_tmdb_payload_to_omdb_movie,
    get_movie_from_tmdb,
    lookup_imdb_id_via_tmdb,
    search_tmdb_match,
)


class LookupImdbIdViaTmdbTests(SimpleTestCase):
    @override_settings(TMDB_API_KEY='')
    def test_returns_none_without_api_key(self):
        self.assertIsNone(lookup_imdb_id_via_tmdb('The Matrix', '1999'))

    @override_settings(TMDB_API_KEY='tmdb-key')
    @patch('movie.tmdb_client.fetch_tmdb_imdb_id', return_value='tt0133093')
    @patch('movie.tmdb_client.requests.get')
    def test_returns_imdb_id_from_best_tmdb_match(self, mock_get, _mock_external_ids):
        response = mock_get.return_value
        response.ok = True
        response.json.return_value = {
            'results': [
                {'id': 603, 'title': 'The Matrix', 'release_date': '1999-03-31'},
            ]
        }

        self.assertEqual(lookup_imdb_id_via_tmdb('The Matrix', '1999'), 'tt0133093')


class MapTmdbPayloadTests(SimpleTestCase):
    def test_maps_movie_payload_to_omdb_dto(self):
        payload = {
            'title': 'The Matrix',
            'release_date': '1999-03-31',
            'runtime': 136,
            'overview': 'Neo learns the truth.',
            'poster_path': '/abc.jpg',
            'vote_average': 8.2,
            'vote_count': 24000,
            'genres': [{'name': 'Action'}],
            'spoken_languages': [{'english_name': 'English'}],
            'production_countries': [{'name': 'United States of America'}],
            'external_ids': {'imdb_id': 'tt0133093'},
            'credits': {
                'cast': [{'name': 'Keanu Reeves'}],
                'crew': [{'name': 'Lana Wachowski', 'job': 'Director'}],
            },
        }

        movie = _map_tmdb_payload_to_omdb_movie(payload, 'movie')
        self.assertEqual(movie.title, 'The Matrix')
        self.assertEqual(movie.year, '1999')
        self.assertEqual(movie.imdb_id, 'tt0133093')
        self.assertEqual(movie.poster, 'https://image.tmdb.org/t/p/w500/abc.jpg')
        self.assertIsNone(movie.imdb_rating)
        self.assertEqual(movie.ratings[0].source, 'TMDB')


class GetMovieFromTmdbTests(SimpleTestCase):
    @override_settings(TMDB_API_KEY='tmdb-key')
    @patch('movie.tmdb_client.requests.get')
    def test_fetches_and_maps_details(self, mock_get):
        response = mock_get.return_value
        response.ok = True
        response.json.return_value = {
            'title': 'Inception',
            'release_date': '2010-07-16',
            'overview': 'Dreams.',
            'genres': [{'name': 'Science Fiction'}],
            'external_ids': {'imdb_id': 'tt1375666'},
            'credits': {'cast': [], 'crew': []},
        }

        movie = get_movie_from_tmdb('movie', 27205)
        self.assertEqual(movie.title, 'Inception')
        self.assertEqual(movie.imdb_id, 'tt1375666')
        mock_get.assert_called_once()


class SearchTmdbMatchTests(SimpleTestCase):
    @override_settings(TMDB_API_KEY='tmdb-key')
    @patch('movie.tmdb_client.fetch_tmdb_imdb_id', return_value='tt0133093')
    @patch('movie.tmdb_client.requests.get')
    def test_returns_best_match(self, mock_get, _mock_fetch_imdb):
        response = mock_get.return_value
        response.ok = True
        response.json.return_value = {
            'results': [
                {'id': 603, 'title': 'The Matrix', 'release_date': '1999-03-31'},
            ]
        }

        match = search_tmdb_match('The Matrix', '1999')
        self.assertIsNotNone(match)
        self.assertEqual(match.tmdb_id, 603)
        self.assertEqual(match.imdb_id, 'tt0133093')
