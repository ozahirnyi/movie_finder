from unittest.mock import patch

from allauth.socialaccount.models import SocialAccount, SocialApp, SocialLogin
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from auth_app.errors import ChangePasswordError
from auth_app.serializers import SignUpSerializer


class AuthTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.signup_data = {
            'email': 'test@test.test',
            'password': 'test_pass123',
        }

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email='neo@neo.neo', password='neoneoneo')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}',
            HTTP_USER_AGENT='test-agent',
        )

    def test_signup(self):
        response = self.client.post(reverse('signup'), data=self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_user_already_exist(self):
        self.assertEqual(self.client.post(reverse('signup'), data=self.signup_data).status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('signup'), data=self.signup_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin(self):
        self.client.post(reverse('signup'), data=self.signup_data)

        response = self.client.post(reverse('token_obtain_pair'), data=self.signup_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_change_password(self):
        new_data = {
            'old_password': 'neoneoneo',
            'new_password': 'test_new_pass',
        }

        response = self.client.patch(reverse('change_password'), data=new_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(new_data['new_password']))

    def test_change_password_wrong_old(self):
        response = self.client.patch(
            reverse('change_password'),
            data={'old_password': 'wrongpass', 'new_password': 'test_new_pass'},
        )
        default_code = response.data['detail'].code
        default_detail = response.data['detail']

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
            provider='google',
            name='Google',
            client_id='test-client-id',
            secret='test-client-secret',
        )
        app.sites.add(site)

    def setUp(self):
        """Initialize test client and URLs."""
        self.client = Client()
        self.login_url = '/accounts/google/login/'
        self.callback_url = '/accounts/google/login/callback/'
        self.redirect_url = '/'

    @patch('allauth.socialaccount.providers.google.views.requests.post')
    def test_google_login_success(self, mock_post):
        """Tests Google login, user creation, authentication, and redirection."""
        mock_post.return_value.json.return_value = {
            'access_token': 'test_access_token',
            'id_token': 'test_id_token',
        }

        with patch.object(GoogleOAuth2Adapter, 'complete_login') as mock_complete_login:
            test_user = User.objects.create_user(email='testuser@gmail.com')

            social_account = SocialAccount(
                provider='google',
                uid='123456789',
                user=test_user,
                extra_data={
                    'email': 'testuser@gmail.com',
                    'verified_email': True,
                    'name': 'Test User',
                },
            )
            social_account.save()

            sociallogin = SocialLogin(user=test_user, account=social_account)
            mock_complete_login.return_value = sociallogin

            response = self.client.get(self.login_url)
            self.assertEqual(response.status_code, 200)

            response = self.client.post(self.callback_url)
            self.assertEqual(response.status_code, 200)

            response = self.client.get(self.redirect_url)
            self.assertEqual(response.status_code, 404)  # We have no "/" url on the backend

            user = User.objects.get(email='testuser@gmail.com')
            self.assertEqual(user.email, 'testuser@gmail.com')
            self.assertTrue(user.is_active)

            social_account = SocialAccount.objects.filter(user=test_user).first()
            self.assertIsNotNone(social_account)


class UserManagerTests(TestCase):
    def test_create_user_without_email_raises(self):
        with self.assertRaises(TypeError):
            User.objects.create_user(email=None, password='validpass')

    def test_create_superuser_without_password_raises(self):
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email='admin@test.test', password=None)

    def test_create_superuser_sets_staff_flags(self):
        user = User.objects.create_superuser(email='admin@test.test', password='validpass')

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password('validpass'))


class SignUpSerializerTests(TestCase):
    def test_validate_email_duplicates(self):
        User.objects.create_user(email='duplicate@test.test', password='validpass')

        serializer = SignUpSerializer(data={'email': 'duplicate@test.test', 'password': 'validpass'})

        self.assertFalse(serializer.is_valid())
        self.assertIn('A user with that email already exists.', serializer.errors['email'])

    def test_validate_password_errors_are_wrapped(self):
        serializer = SignUpSerializer(data={'email': 'new@test.test', 'password': 'password'})

        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)
