from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_find_movie(self):
        data = {'expression': 'Shrek'}
        self.client.request()
        response = self.client.get(path=reverse('find-movie'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
