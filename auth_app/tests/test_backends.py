from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from rest_framework import exceptions

from auth_app.backends import JWTAuthentication


class JWTAuthenticationTests(TestCase):
    def setUp(self) -> None:
        self.backend = JWTAuthentication()
        self.factory = RequestFactory()
        self.user_model = get_user_model()

    def _make_request(self, header_value: str | None):
        request = self.factory.get('/auth-test')
        if header_value is not None:
            request.META['HTTP_AUTHORIZATION'] = header_value
        return request

    def test_returns_none_when_header_missing_or_malformed(self) -> None:
        request_without_header = self._make_request(None)
        self.assertIsNone(self.backend.authenticate(request_without_header))

        request_single_segment = self._make_request('Token')
        self.assertIsNone(self.backend.authenticate(request_single_segment))

        request_extra_segment = self._make_request('Token one two')
        self.assertIsNone(self.backend.authenticate(request_extra_segment))

        request_wrong_prefix = self._make_request('Bearer sometoken')
        self.assertIsNone(self.backend.authenticate(request_wrong_prefix))

    def test_decode_errors_raise_authentication_failed(self) -> None:
        request = self._make_request('Token sometoken')

        with patch('auth_app.backends.jwt.decode', side_effect=Exception('boom')):
            with self.assertRaises(exceptions.AuthenticationFailed):
                self.backend.authenticate(request)

    def test_unknown_user_and_inactive_user_raise_authentication_failed(self) -> None:
        request = self._make_request('Token sometoken')

        with patch('auth_app.backends.jwt.decode', return_value={'id': 999}):
            with self.assertRaises(exceptions.AuthenticationFailed):
                self.backend.authenticate(request)

        inactive_user = self.user_model.objects.create_user(email='inactive@test.test', password='pass123')
        inactive_user.is_active = False
        inactive_user.save(update_fields=['is_active'])
        with patch('auth_app.backends.jwt.decode', return_value={'id': inactive_user.id}):
            with self.assertRaises(exceptions.AuthenticationFailed):
                self.backend.authenticate(request)

    def test_successful_authentication_returns_user_and_token(self) -> None:
        user = self.user_model.objects.create_user(email='active@test.test', password='pass123')
        request = self._make_request('Token validtoken')

        with patch('auth_app.backends.jwt.decode', return_value={'id': user.id}):
            authenticated_user, returned_token = self.backend.authenticate(request)

        self.assertEqual(authenticated_user, user)
        self.assertEqual(returned_token, 'validtoken')
