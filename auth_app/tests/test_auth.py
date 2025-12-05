from importlib import import_module
from unittest.mock import patch

from allauth.socialaccount.models import SocialAccount, SocialApp, SocialLogin
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.apps import apps as django_apps
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from auth_app.admin import AccountTierAdmin
from auth_app.errors import ChangePasswordError
from auth_app.forms import UserChangeForm, UserCreationForm
from auth_app.models import AccountTier
from auth_app.repositories import AccountTierRepository
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


class UserFormTests(TestCase):
    def setUp(self):
        self.account_tier = AccountTier.objects.create(
            code='forms-tier',
            name='Forms Tier',
            daily_ai_search_limit=1,
            is_default=False,
        )

    def test_user_creation_form_requires_matching_passwords(self):
        form = UserCreationForm(
            data={
                'email': 'forms@example.com',
                'account_tier': self.account_tier.pk,
                'is_staff': False,
                'is_superuser': False,
                'password1': 'StrongPass123',
                'password2': 'MismatchPass123',
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn('Passwords do not match.', form.errors['password2'])

    def test_user_creation_form_saves_hashed_password(self):
        form = UserCreationForm(
            data={
                'email': 'created@example.com',
                'account_tier': self.account_tier.pk,
                'is_staff': True,
                'is_superuser': False,
                'password1': 'MatchingPass123!',
                'password2': 'MatchingPass123!',
            }
        )

        self.assertTrue(form.is_valid())
        user = form.save()

        self.assertNotEqual(user.password, 'MatchingPass123!')
        self.assertTrue(user.check_password('MatchingPass123!'))

    def test_user_change_form_returns_initial_password(self):
        user = User.objects.create_user(email='change@example.com', password='ChangePass123!')
        form = UserChangeForm(
            instance=user,
            data={
                'email': user.email,
                'password': user.password,
                'account_tier': user.account_tier.pk,
                'is_active': user.is_active,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
            },
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['password'], user.password)


class AccountTierAdminTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.admin_site = AdminSite()
        self.account_tier = AccountTier.objects.create(
            code='admin-tier',
            name='Admin Tier',
            daily_ai_search_limit=5,
            is_default=True,
        )
        self.admin = AccountTierAdmin(AccountTier, self.admin_site)

    def test_save_model_enforces_single_default(self):
        request = self.factory.post('/admin/auth_app/accounttier/')
        with patch('auth_app.admin.AccountTierRepository') as repo_cls:
            repo_instance = repo_cls.return_value
            self.admin.save_model(request, self.account_tier, form=None, change=True)

        repo_instance.enforce_single_default.assert_called_once_with(self.account_tier)


class AccountTierModelTests(TestCase):
    def test_str_includes_quota(self):
        tier = AccountTier.objects.create(
            code='string-tier',
            name='String Tier',
            daily_ai_search_limit=7,
            is_default=False,
        )

        self.assertEqual(str(tier), 'String Tier (7/day)')


class AccountTierRepositoryTests(TestCase):
    def setUp(self):
        get_user_model().objects.all().delete()
        AccountTier.objects.all().delete()
        self.repo = AccountTierRepository()

    def test_resolve_returns_explicit_tier(self):
        tier = AccountTier.objects.create(code='explicit', name='Explicit', daily_ai_search_limit=1, is_default=False)

        self.assertEqual(self.repo.resolve(tier), tier)

    def test_resolve_prefers_default_tier(self):
        default_tier = AccountTier.objects.create(code='default', name='Default', daily_ai_search_limit=2, is_default=True)
        AccountTier.objects.create(code='other', name='Other', daily_ai_search_limit=3, is_default=False)

        self.assertEqual(self.repo.resolve(None), default_tier)

    def test_resolve_falls_back_to_first_when_no_default(self):
        fallback = AccountTier.objects.create(code='fallback', name='Fallback', daily_ai_search_limit=4, is_default=False)
        AccountTier.objects.create(code='secondary', name='Secondary', daily_ai_search_limit=5, is_default=False)

        self.assertEqual(self.repo.resolve(None), fallback)

    def test_resolve_raises_when_no_tiers_exist(self):
        AccountTier.objects.all().delete()

        with self.assertRaises(ValueError):
            self.repo.resolve(None)

    def test_enforce_single_default_disables_other_defaults(self):
        primary = AccountTier.objects.create(code='primary', name='Primary', daily_ai_search_limit=5, is_default=True)
        secondary = AccountTier.objects.create(code='secondary-default', name='Secondary', daily_ai_search_limit=6, is_default=True)

        self.repo.enforce_single_default(primary)
        secondary.refresh_from_db()

        self.assertFalse(secondary.is_default)


class AccountTierMigrationTests(TestCase):
    def setUp(self):
        self.UserModel = get_user_model()
        self.UserModel.objects.all().delete()
        self.migration_module = import_module('auth_app.migrations.0002_account_tiers')
        self.AccountTierModel = django_apps.get_model('auth_app', 'AccountTier')

    def test_create_account_tiers_updates_existing_records(self):
        AccountTier = self.AccountTierModel
        AccountTier.objects.all().delete()
        tier = AccountTier.objects.create(code='premium', name='Old Premium', daily_ai_search_limit=1, is_default=True)

        self.migration_module.create_account_tiers(django_apps, None)
        tier.refresh_from_db()

        self.assertEqual(tier.daily_ai_search_limit, 30)
        self.assertFalse(tier.is_default)
        self.assertTrue(AccountTier.objects.filter(code='free').exists())

    def test_create_account_tiers_falls_back_when_default_missing(self):
        AccountTier = self.AccountTierModel
        AccountTier.objects.all().delete()
        fallback = AccountTier.objects.create(code='free', name='Fallback Free', daily_ai_search_limit=9, is_default=False)

        original_get_or_create = AccountTier.objects.get_or_create
        original_filter = AccountTier.objects.filter
        filter_called = {'free': False}

        def fake_get_or_create(*args, **kwargs):
            if kwargs.get('code') == 'free':
                return None, True
            return original_get_or_create(*args, **kwargs)

        def instrumented_filter(*args, **kwargs):
            if kwargs.get('code') == 'free':
                filter_called['free'] = True
            return original_filter(*args, **kwargs)

        with (
            patch.object(AccountTier.objects, 'get_or_create', side_effect=fake_get_or_create),
            patch.object(
                AccountTier.objects,
                'filter',
                side_effect=instrumented_filter,
            ),
        ):
            self.migration_module.create_account_tiers(django_apps, None)

        self.assertTrue(filter_called['free'])
        fallback.refresh_from_db()
        self.assertFalse(AccountTier.objects.exclude(pk=fallback.pk).filter(is_default=True).exists())


class DefaultAdminMigrationTests(TestCase):
    def setUp(self):
        self.UserModel = get_user_model()
        self.AccountTierModel = django_apps.get_model('auth_app', 'AccountTier')
        self.migration_module = import_module('auth_app.migrations.0003_default_admin')
        self.UserModel.objects.all().delete()
        self.admin_tier, _ = self.AccountTierModel.objects.get_or_create(
            code='admin',
            defaults={'name': 'Admin', 'daily_ai_search_limit': 100, 'is_default': False},
        )

    def test_create_default_admin_noop_when_exists(self):
        existing = self.UserModel.objects.create(email='admin@admin.com', account_tier=self.admin_tier)

        self.migration_module.create_default_admin(django_apps, None)

        self.assertEqual(self.UserModel.objects.filter(email='admin@admin.com').count(), 1)
        self.assertEqual(self.UserModel.objects.get(email='admin@admin.com').id, existing.id)

    def test_delete_default_admin_removes_user(self):
        self.UserModel.objects.create(email='admin@admin.com', account_tier=self.admin_tier)

        self.migration_module.delete_default_admin(django_apps, None)

        self.assertFalse(self.UserModel.objects.filter(email='admin@admin.com').exists())
