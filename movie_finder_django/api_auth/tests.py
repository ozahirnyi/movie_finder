from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.views import exception_handler
from rest_framework_simplejwt.tokens import RefreshToken

from api_auth.errors import ChangePasswordError


class AuthTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.register_data = {'email': 'test@test.test', 'username': 'Shrek', 'password': 'test_pass'}
        cls.login_data = {'email': 'test@test.test', 'password': 'test_pass'}
        cls.pass_change_data = {'password': 'test_pass', 'newPassword': 'test_new_pass',
                                'newPasswordConfirmation': 'test_new_pass'}

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='neo', email='neo@neo.neo', password='neoneoneo')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_register(self):
        response = self.client.post(reverse('register'), data=self.register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_already_exist(self):
        response = self.client.post(reverse('register'), data=self.register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('register'), data=self.register_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        response = self.client.post(reverse('register'), data=self.register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('login'), data=self.login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        new_data = {
            'email': 'new_test@new.test',
            'username': 'newusername',
            'password': 'newpassword',
        }
        response = self.client.patch(reverse('user'), data=new_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, new_data['email'])

    def test_change_password(self):
        old_password = 'neoneoneo'
        new_data = {
            'old_password': old_password,
            'new_password': 'test_new_pass',
        }

        response = self.client.patch(reverse('change_password'), data=new_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertNotEqual(self.user.password, old_password)

    def test_change_password_wrong_old(self):
        old_password = 'neoneoneo-wrong'
        new_data = {
            'old_password': old_password,
            'new_password': 'test_new_pass',
        }
        response = self.client.patch(reverse('change_password'), data=new_data)
        default_code = response.data['detail'].code
        default_detail = response.data['detail']

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(default_code, ChangePasswordError.default_code)
        self.assertEqual(default_detail, ChangePasswordError.default_detail)