from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from .models import Movie


class FinderTests(APITestCase):

    def test_find_movie(self):
        self.client.login(
            email='test_email@test.email',
            username='test',
            password='test_pass',
        )
        response = self.client.get(reverse('find_movie', kwargs={'expression': 'Shrek'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Movie.objects.get(id=response.data[0]['id']))
