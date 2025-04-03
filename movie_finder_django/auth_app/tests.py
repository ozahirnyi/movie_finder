from unittest.mock import patch

from allauth.socialaccount.models import SocialApp, SocialAccount, SocialLogin
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.test import TestCase, Client
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
            email="neo@neo.neo", password="neoneoneo"
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


User = get_user_model()


class GoogleOAuthTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Ensure Google OAuth SocialApp is set up for tests."""
        site = Site.objects.get_current()
        app, _ = SocialApp.objects.get_or_create(
            provider="google",
            name="Google",
            client_id="test-client-id",
            secret="test-client-secret",
        )
        app.sites.add(site)

    def setUp(self):
        """Initialize test client and URLs."""
        self.client = Client()
        self.login_url = "/accounts/google/login/"
        self.callback_url = "/accounts/google/login/callback/"
        self.redirect_url = "/"

    @patch("allauth.socialaccount.providers.google.views.requests.post")
    def test_google_login_success(self, mock_post):
        """Tests Google login, user creation, authentication, and redirection."""
        mock_post.return_value.json.return_value = {
            "access_token": "test_access_token",
            "id_token": "test_id_token"
        }

        with patch.object(GoogleOAuth2Adapter, 'complete_login') as mock_complete_login:
            test_user = User.objects.create_user(
                email="testuser@gmail.com"
            )

            social_account = SocialAccount(
                provider='google',
                uid='123456789',
                user=test_user,
                extra_data={
                    'email': 'testuser@gmail.com',
                    'verified_email': True,
                    'name': 'Test User'
                }
            )
            social_account.save()

            sociallogin = SocialLogin(
                user=test_user,
                account=social_account
            )
            mock_complete_login.return_value = sociallogin

            response = self.client.get(self.login_url)
            self.assertEqual(response.status_code, 200)

            response = self.client.post(self.callback_url)
            self.assertEqual(response.status_code, 200)

            response = self.client.get(self.redirect_url)
            self.assertEqual(response.status_code, 404)  # We have no "/" url on the backend

            user = User.objects.get(email="testuser@gmail.com")
            self.assertEqual(user.email, "testuser@gmail.com")
            self.assertTrue(user.is_active)

            social_account = SocialAccount.objects.get(user=user)
            self.assertEqual(social_account.provider, 'google')
            self.assertEqual(social_account.uid, '123456789')
