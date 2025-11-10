from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase

from collection.admin import CollectionAdmin
from collection.models import Collection, CollectionMovie
from movie.models import Movie


class CollectionAdminTests(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = CollectionAdmin(Collection, self.site)
        self.user = get_user_model().objects.create_user(email='admin-test@example.com', password='pass1234')
        self.movie = Movie.objects.create(title='Admin Movie', imdb_id='tt6000001')

    def test_movies_count(self):
        collection = Collection.objects.create(owner=self.user, name='Count Me', description='', is_public=False)
        CollectionMovie.objects.create(collection=collection, movie=self.movie)

        self.assertEqual(self.admin.movies_count(collection), 1)
