from django.contrib.auth import get_user_model
from django.test import TestCase

from collection.models import Collection, CollectionMovie
from movie.models import Movie


class CollectionModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='model@example.com', password='pass1234')
        self.movie = Movie.objects.create(title='Model Movie', imdb_id='tt5000001')

    def test_collection_str(self):
        collection = Collection.objects.create(owner=self.user, name='Model Collection', description='', is_public=False)
        self.assertIn('Model Collection', str(collection))

    def test_collection_movie_str(self):
        collection = Collection.objects.create(owner=self.user, name='Has Relation', description='', is_public=False)
        relation = CollectionMovie.objects.create(collection=collection, movie=self.movie)
        self.assertEqual(str(relation), f'{collection.id}:{self.movie.id}')

    def test_collection_subscription_str(self):
        collection = Collection.objects.create(owner=self.user, name='Subscribable', description='', is_public=True)
        subscription = collection.subscriptions.create(user=self.user)
        self.assertEqual(str(subscription), f'{collection.id}:{self.user.id}')
