from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .errors import ChangePasswordError


class AuthTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.signup_data = {
            "email": "test@test.test",
            "username": "Shrek",
            "password": "test_pass",
        }
        cls.signin_data = {"email": "test@test.test", "password": "test_pass"}

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="neo", email="neo@neo.neo", password="neoneoneo"
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_signup(self):
        response = self.client.post(reverse("signup"), data=self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_user_already_exist(self):
        response = self.client.post(reverse("signup"), data=self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse("signup"), data=self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin(self):
        response = self.client.post(reverse("signup"), data=self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse("signin"), data=self.signin_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        new_data = {
            "email": "new_test@new.test",
            "username": "newusername",
            "password": "newpassword",
        }
        response = self.client.patch(reverse("user"), data=new_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, new_data["email"])

    def test_change_password(self):
        new_data = {
            "old_password": "neoneoneo",
            "new_password": "test_new_pass",
        }

        response = self.client.patch(reverse("change_password"), data=new_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertNotEqual(self.user.password, new_data["old_password"])

    def test_change_password_wrong_old(self):
        new_data = {
            "old_password": "neoneoneo-wrong",
            "new_password": "test_new_pass",
        }
        response = self.client.patch(reverse("change_password"), data=new_data)
        default_code = response.data["detail"].code
        default_detail = response.data["detail"]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(default_code, ChangePasswordError.default_code)
        self.assertEqual(default_detail, ChangePasswordError.default_detail)
