from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Movie, WatchLater


class FinderTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(title='test', imdb_id='test')

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='neo', email='neo@neo.neo', password='neoneoneo')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_find_movie(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('find_movie', kwargs={'expression': 'Shrek'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Movie.objects.get(id=response.data[0]['id']))

    def test_create_watch_later(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('watch_later_create'), data={'movie': self.movie.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        wl = WatchLater.objects.filter(user=self.user, movie=self.movie)
        self.assertTrue(wl.exists())

    def test_delete_watch_later(self):
        wl = WatchLater.objects.create(user=self.user, movie=self.movie)

        self.client.force_login(self.user)
        response = self.client.delete(reverse('watch_later_destroy', kwargs={'pk': wl.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        wl = WatchLater.objects.filter(user=self.user, movie=self.movie)
        self.assertFalse(wl.exists())

    def test_get_watch_later(self):
        WatchLater.objects.create(user=self.user, movie=self.movie)

        self.client.force_login(self.user)
        response = self.client.get(reverse('watch_later_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['user'], self.user.id)
