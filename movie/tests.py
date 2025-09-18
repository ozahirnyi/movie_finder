import random
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from movie.dataclasses import AiMovie, ImdbMovie
from movie.errors import AddLikeError
from movie.models import LikeMovie, Movie, WatchLaterMovie


class FinderTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(title='test', imdb_id='1')

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email='neo@neo.neo', password='neoneoneo')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}',
            HTTP_USER_AGENT='test-agent',
            HTTP_X_FORWARDED_FOR='127.0.0.1',
        )

    def test_get_movie(self):
        with self.assertNumQueries(2):
            response = self.client.get(reverse('movie', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_movie(self):
        self.client.force_login(self.user)
        with self.assertNumQueries(2):
            response = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_like_movie_error(self):
        self.client.force_login(self.user)
        with self.assertNumQueries(2):
            response = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        with self.assertNumQueries(2):
            response = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        default_code = response.data['detail'].code
        default_detail = response.data['detail']
        self.assertEqual(default_code, AddLikeError.default_code)
        self.assertEqual(default_detail, AddLikeError.default_detail)

    def test_unlike_movie(self):
        LikeMovie.objects.create(user=self.user, movie=self.movie)
        self.client.force_login(self.user)
        with self.assertNumQueries(2):
            response = self.client.post(reverse('movie_unlike', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('movie.services.MovieService.get_movies_from_imdb')
    def test_find_movie(self, mock_get_movies_from_imdb):
        mock_get_movies_from_imdb.return_value = [
            ImdbMovie(
                title='Shrek',
                imdb_id='12345',
                poster='http://poster.url',
                year='2001',
                type='movie',
            ),
        ]
        with self.assertNumQueries(4):
            response = self.client.get(reverse('find_movie'), {'expression': 'Shrek'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_watch_later(self):
        self.client.force_login(self.user)
        with self.assertNumQueries(3):
            response = self.client.post(reverse('watch_later_create'), data={'movie': self.movie.id})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        wl = WatchLaterMovie.objects.filter(user=self.user, movie=self.movie)
        self.assertTrue(wl.exists())

    def test_delete_watch_later(self):
        wl = WatchLaterMovie.objects.create(user=self.user, movie=self.movie)

        self.client.force_login(self.user)
        with self.assertNumQueries(2):
            response = self.client.delete(reverse('watch_later_destroy', kwargs={'pk': wl.movie.id}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        wl = WatchLaterMovie.objects.filter(user=self.user, movie=self.movie)
        self.assertFalse(wl.exists())

    def test_get_watch_later(self):
        wrong_user = get_user_model().objects.create_user(email='notneo@neo.neo', password='neoneoneo')
        WatchLaterMovie.objects.create(user_id=wrong_user.id, movie_id=self.movie.id)
        WatchLaterMovie.objects.create(user_id=self.user.id, movie_id=self.movie.id)

        self.client.force_login(self.user)
        with self.assertNumQueries(3):
            response = self.client.get(reverse('watch_later_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data['results'][0]
        self.assertTrue(response_data['is_watch_later'])
        self.assertEqual(response_data['watch_later_count'], 2)


class FindMovieAiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='neo@neo.neo', password='neoneoneo')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}',
            HTTP_USER_AGENT='test-agent',
            HTTP_X_FORWARDED_FOR='127.0.0.1',
        )

    @patch('movie.ai_find_movie.FindMovieAiClient.find_movies')
    @patch('movie.services.MovieService.get_movies_from_imdb')
    def test_find_movie_ai(self, mock_get_movies_from_imdb, mock_find_movies):
        mock_find_movies.return_value = [
            AiMovie(title='Shrek', genre='Animation', plot='A green ogre saves a princess.'),
            AiMovie(title='Shrek 2', genre='Animation', plot='The ogre meets his in-laws.'),
        ]

        def mock_get_movies(title):
            movies = {
                'Shrek': ImdbMovie(
                    title='Shrek',
                    imdb_id='12345',
                    poster='http://poster.url',
                    year='2001',
                    type='movie',
                ),
                'Shrek 2': ImdbMovie(
                    title='Shrek 2',
                    imdb_id='67890',
                    poster='http://poster.url',
                    year='2004',
                    type='movie',
                ),
            }
            return [movies.get(title)] if title in movies else []

        mock_get_movies_from_imdb.side_effect = mock_get_movies

        response = self.client.post(
            reverse('find_movie_ai'),
            data={'prompt': 'Shrek'},
            format='json',
            HTTP_USER_AGENT='test-agent',
            HTTP_X_FORWARDED_FOR='127.0.0.1',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        movie = response.data[0]
        self.assertEqual(movie['title'], 'Shrek')
        self.assertEqual(movie['genre'], 'Animation')
        self.assertEqual(movie['plot'], 'A green ogre saves a princess.')
        self.assertEqual(movie['imdb_id'], '12345')

        self.assertTrue(Movie.objects.filter(title='Shrek').exists())

    def test_prompt_max_length(self):
        max_length = 255

        long_prompt = 'A' * (max_length + 1)

        response = self.client.post(
            reverse('find_movie_ai'),
            data={'prompt': long_prompt},
            HTTP_USER_AGENT='test-agent',
            HTTP_X_FORWARDED_FOR='127.0.0.1',
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('prompt', response.data)
        self.assertEqual(
            response.data['prompt'][0],
            f'Ensure this field has no more than {max_length} characters.',
        )  # Check if the correct validation message is returned


class FindMovieFiltersTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.shrek = Movie.objects.create(title='Shrek', imdb_id='1', year='2001', genre='Comedy')
        cls.shrek_2 = Movie.objects.create(title='Shrek 2', imdb_id='2', year='2004', genre='Animation')
        cls.user = get_user_model().objects.create_user(email='neo@neo.neo', password='neoneoneo')
        LikeMovie.objects.create(user_id=cls.user.id, movie_id=cls.shrek.id)

    def setUp(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}',
            HTTP_USER_AGENT=f'test-agent{random.randint(0, 1000)}',
            HTTP_X_FORWARDED_FOR=f'127.0.0.{random.randint(0, 1000)}',
        )

    def test_filter_by_title(self):
        response = self.client.get(reverse('find_movie'), {'title': 'shrek 2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Shrek 2')

    def test_filter_by_genre(self):
        response = self.client.get(reverse('find_movie'), {'genre': 'Animation'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Shrek 2')

    def test_filter_by_year(self):
        response = self.client.get(reverse('find_movie'), {'year': '2001'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Shrek')

    def test_filter_by_imdb_id(self):
        response = self.client.get(reverse('find_movie'), {'imdb_id': '1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Shrek')

    def test_sorting_by_title(self):
        response = self.client.get(reverse('find_movie'), {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [movie['title'] for movie in response.data['results']]
        self.assertEqual(titles, sorted(titles))

    def test_sorting_by_year(self):
        response = self.client.get(reverse('find_movie'), {'ordering': 'year'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [int(movie['year']) for movie in response.data['results']]
        self.assertEqual(years, sorted(years))

    def test_sorting_by_imdb_id(self):
        response = self.client.get(reverse('find_movie'), {'ordering': 'imdb_id'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        imdb_ids = [movie['imdb_id'] for movie in response.data['results']]
        self.assertEqual(imdb_ids, sorted(imdb_ids))

    def test_sorting_by_genre(self):
        response = self.client.get(reverse('find_movie'), {'genre': 'Comedy'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        genres = [movie['genre'] if movie['genre'] else '' for movie in response.data['results']]
        self.assertEqual(genres, sorted(genres))

    def test_sorting_by_likes_count(self):
        response = self.client.get(reverse('find_movie'), {'ordering': 'likes_count'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        likes_counts = [movie['likes_count'] for movie in response.data['results']]
        self.assertEqual(likes_counts, sorted(likes_counts))
        response = self.client.get(reverse('find_movie'), {'ordering': '-likes_count'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        likes_counts = [movie['likes_count'] for movie in response.data['results']]
        self.assertEqual(likes_counts, sorted(likes_counts, reverse=True))

    def test_sorting_by_default(self):
        response = self.client.get(reverse('find_movie'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        imdb_ids = [movie['imdb_id'] for movie in response.data['results']]
        self.assertEqual(imdb_ids, sorted(imdb_ids))
