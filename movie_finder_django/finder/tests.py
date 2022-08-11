from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from .errors import FindMovieNotExist
from .models import Movie


class AccountTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.auth_data = {'username': 'Shrek', 'password': 'test'}
        cls.admin_user = get_user_model().objects.create(
            email='test_email@test.email',
            is_superuser=True,
        )

    def test_find_movie(self):
        self.client.force_login(self.admin_user)
        response = self.client.get(reverse('find_movie', kwargs={'expression': 'Shrek'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Movie.objects.get(id=response.data[0]['id']))

    def test_register(self):
        response = self.client.post(reverse('register'), data=self.auth_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        response = self.client.post(reverse('register'), data=self.auth_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

        response = self.client.post(reverse('login'), data=self.auth_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
