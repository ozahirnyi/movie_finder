from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
<<<<<<< HEAD

=======
>>>>>>> afa1bd3d57b760786e9d1fd1f85aa34f2f4027fb
from .errors import AddLikeError
from .models import Movie, WatchLaterMovie, LikeMovie


class FinderTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(title='test', imdb_id='1')

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='neo', email='neo@neo.neo', password='neoneoneo')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

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
<<<<<<< HEAD
        with self.assertNumQueries(4):
            response = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
            response2 = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
            response2 = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
        likes = LikeMovie.objects.filter(user=self.user, movie=self.movie)
        default_code = response.data['detail'].code
        default_detail = response.data['detail']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
=======
        with self.assertNumQueries(2):
            response = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        with self.assertNumQueries(2):
            response = self.client.post(reverse('movie_like', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        default_code = response.data['detail'].code
        default_detail = response.data['detail']
>>>>>>> afa1bd3d57b760786e9d1fd1f85aa34f2f4027fb
        self.assertEqual(default_code, AddLikeError.default_code)
        self.assertEqual(default_detail, AddLikeError.default_detail)

    def test_unlike_movie(self):
        LikeMovie.objects.create(user=self.user, movie=self.movie)
        self.client.force_login(self.user)
        with self.assertNumQueries(2):
            response = self.client.post(reverse('movie_unlike', kwargs={'id': self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_find_movie(self):
        # TODO: uncomment when start use postgresql. > movie_finder_django/api/models.py
        # with self.assertNumQueries(3):
        response = self.client.get(reverse('find_movie', kwargs={'expression': 'Shrek'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_watch_later(self):
        self.client.force_login(self.user)
        with self.assertNumQueries(3):
            response = self.client.post(reverse('watch_later_create'), data={'movie': self.movie.imdb_id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        wl = WatchLaterMovie.objects.filter(user=self.user, movie=self.movie)
        self.assertTrue(wl.exists())

    def test_delete_watch_later(self):
        wl = WatchLaterMovie.objects.create(user=self.user, movie=self.movie)

        self.client.force_login(self.user)
        with self.assertNumQueries(3):
            response = self.client.delete(reverse('watch_later_destroy', kwargs={'pk': wl.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        wl = WatchLaterMovie.objects.filter(user=self.user, movie=self.movie)
        self.assertFalse(wl.exists())

    def test_get_watch_later(self):
        WatchLaterMovie.objects.create(user=self.user, movie=self.movie)
        wrong_user = get_user_model().objects.create_user(username='notneo', email='notneo@neo.neo', password='neoneoneo')
        WatchLaterMovie.objects.create(user=wrong_user, movie=self.movie)

        self.client.force_login(self.user)
        with self.assertNumQueries(3):
            response = self.client.get(reverse('watch_later_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
