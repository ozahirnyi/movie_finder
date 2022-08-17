from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.auth_data = {'username': 'Shrek', 'password': 'test'}

    def test_register(self):
        response = self.client.post(reverse('register'), data=self.auth_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_already_exist(self):
        response = self.client.post(reverse('register'), data=self.auth_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('register'), data=self.auth_data)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_login(self):
        response = self.client.post(reverse('register'), data=self.auth_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

        response = self.client.post(reverse('login'), data=self.auth_data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
