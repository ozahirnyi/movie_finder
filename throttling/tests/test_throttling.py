from types import SimpleNamespace

from django.test import RequestFactory, SimpleTestCase
from rest_framework.exceptions import ValidationError

from throttling.throttling import RegularSearchForwardedThrottle, RegularSearchIpThrottle, RegularSearchUaThrottle


class ThrottlingTests(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_ua_throttle_requires_user_agent(self):
        request = self.factory.get('/')
        throttle = RegularSearchUaThrottle()

        with self.assertRaises(ValidationError):
            throttle.get_cache_key(request, view=None)

    def test_forwarded_for_uses_first_ip(self):
        request = self.factory.get('/', HTTP_X_FORWARDED_FOR='203.0.113.10, 10.0.0.2', HTTP_USER_AGENT='agent')
        throttle = RegularSearchForwardedThrottle()

        key = throttle.get_cache_key(request, view=None)

        self.assertTrue(key.endswith('203.0.113.10'))

    def test_forwarded_for_falls_back_to_remote_addr(self):
        request = self.factory.get('/', REMOTE_ADDR='198.51.100.5', HTTP_USER_AGENT='agent')
        throttle = RegularSearchForwardedThrottle()

        key = throttle.get_cache_key(request, view=None)

        self.assertTrue(key.endswith('198.51.100.5'))

    def test_ua_throttle_with_manual_request_object(self):
        request = SimpleNamespace(META={})
        throttle = RegularSearchUaThrottle()

        with self.assertRaises(ValidationError):
            throttle.get_cache_key(request, view=None)

    def test_forwarded_throttle_manual_request(self):
        request = SimpleNamespace(META={'REMOTE_ADDR': '10.0.0.1'})
        throttle = RegularSearchForwardedThrottle()

        key = throttle.get_cache_key(request, view=None)

        self.assertEqual(key, 'throttle_forwarded_10.0.0.1')

    def test_ua_throttle_returns_cache_key(self):
        request = self.factory.get('/', HTTP_USER_AGENT='integration-agent')
        throttle = RegularSearchUaThrottle()

        key = throttle.get_cache_key(request, view=None)

        self.assertEqual(key, 'throttle_ua_integration-agent')

    def test_ip_throttle_returns_cache_key(self):
        request = self.factory.get('/', REMOTE_ADDR='203.0.113.42', HTTP_USER_AGENT='agent')
        throttle = RegularSearchIpThrottle()

        key = throttle.get_cache_key(request, view=None)

        self.assertEqual(key, 'throttle_ip_203.0.113.42')
