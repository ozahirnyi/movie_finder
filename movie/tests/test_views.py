import random
from typing import List
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from movie.dataclasses import AiMovie, ImdbMovie, OmdbMovie
from movie.dataclasses import Genre as GenreDTO
from movie.errors import AddLikeError
from movie.models import Genre, LikeMovie, Movie, Rating, WatchLaterMovie


def _issue_jwt(client, user):
    refresh = RefreshToken.for_user(user)
    client.credentials(
        HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}',
        HTTP_USER_AGENT=f'test-agent{random.randint(0, 1000)}',
        HTTP_X_FORWARDED_FOR=f'127.0.0.{random.randint(1, 254)}',
    )


class FinderTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(title='Test Movie', imdb_id='tt000001')

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

    @patch('movie.views.MovieService.search_movies_in_omdb')
    @patch('movie.views.MovieService.get_movies_from_imdb')
    def test_find_movie(self, mock_imdb, mock_search_omdb):
        mock_imdb.return_value = [
            ImdbMovie(
                title='Shrek',
                imdb_id='tt0126029',
                poster='http://poster.url',
                year='2001',
                type='movie',
            ),
        ]
        mock_search_omdb.return_value = [
            OmdbMovie(title='Shrek', imdb_id='tt0126029', genres=[GenreDTO(name='Animation')]),
        ]

        response = self.client.post(
            reverse('movies_search'),
            data={'expression': 'Shrek'},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Shrek')
        mock_imdb.assert_called_once_with('Shrek')
        mock_search_omdb.assert_called_once()

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


class FindMovieAiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='trinity@matrix.test', password='followthewhiterabbit')
        _issue_jwt(self.client, self.user)

    @patch('movie.views.MovieService.search_movies_in_omdb')
    @patch('movie.views.MovieService.get_movies_from_ai')
    def test_find_movie_ai(self, mock_ai, mock_search):
        mock_ai.return_value = [AiMovie(title='Shrek'), AiMovie(title='Shrek 2')]

        def fake_search(titles: List[str], initiator_id: int):
            results = []
            for idx, title in enumerate(titles, start=1):
                imdb_id = f'tt{idx:07d}'
                movie, _ = Movie.objects.get_or_create(title=title, imdb_id=imdb_id)
                results.append(
                    OmdbMovie(
                        title=movie.title,
                        imdb_id=movie.imdb_id,
                        plot=f'Plot for {title}',
                        genres=[GenreDTO(name='Animation')],
                    )
                )
            return results

        mock_search.side_effect = fake_search

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

    def test_prompt_max_length(self):
        max_length = 255
        payload = {'expression': 'A' * (max_length + 1)}

        response = self.client.post(reverse('movies_ai_search'), data=payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('expression', response.data)
        self.assertIn('Ensure this field has no more than', response.data['expression'][0])


class FindMovieFiltersTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.genre_comedy = Genre.objects.create(name='Comedy')
        cls.genre_animation = Genre.objects.create(name='Animation')

        cls.shrek = Movie.objects.create(title='Shrek', imdb_id='tt000010', year='2001')
        cls.shrek.genres.add(cls.genre_comedy)

        cls.shrek_2 = Movie.objects.create(title='Shrek 2', imdb_id='tt000020', year='2004')
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


class MovieModelRepresentationTests(APITestCase):
    def test_movie_str(self):
        movie = Movie.objects.create(title='Representation Test', imdb_id='tt999999')

        self.assertEqual(str(movie), 'Representation Test')

    def test_user_movie_str(self):
        user = get_user_model().objects.create_user(email='repr@test.test', password='thereisnospoon')
        movie = Movie.objects.create(title='String Movie', imdb_id='tt888888')
        like = LikeMovie.objects.create(user=user, movie=movie)

        self.assertEqual(str(like), f'{user} | {movie}')
