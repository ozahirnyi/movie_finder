from importlib import reload

from django.test import SimpleTestCase


class EntryPointTests(SimpleTestCase):
    def test_asgi_application_is_initialised(self):
        module = reload(__import__('movie_finder_django.asgi', fromlist=['application']))
        self.assertIsNotNone(module.application)

    def test_wsgi_application_is_initialised(self):
        module = reload(__import__('movie_finder_django.wsgi', fromlist=['application']))
        self.assertIsNotNone(module.application)
