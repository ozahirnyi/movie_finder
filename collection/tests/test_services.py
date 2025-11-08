from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from collection.models import Collection, CollectionMovie
from collection.services import CollectionService
from movie.models import Movie


class CollectionServiceTests(TestCase):
    def setUp(self):
        self.service = CollectionService()
        self.owner = get_user_model().objects.create_user(email='owner@example.com', password='pass1234')
        self.another_user = get_user_model().objects.create_user(email='another@example.com', password='pass1234')
        self.admin = get_user_model().objects.create_user(email='admin@example.com', password='pass1234', is_staff=True)

        self.movie_one = Movie.objects.create(title='Movie One', imdb_id='tt000010')
        self.movie_two = Movie.objects.create(title='Movie Two', imdb_id='tt000011')
        self.movie_three = Movie.objects.create(title='Movie Three', imdb_id='tt000012')

    def test_create_collection_with_movies(self):
        dto = self.service.create_collection(
            owner=self.owner,
            name='Favorites',
            description='Top picks',
            is_public=False,
            movie_ids=[self.movie_one.id, self.movie_two.id],
        )

        self.assertEqual(dto.owner_id, self.owner.id)
        self.assertEqual([movie.id for movie in dto.movies], [self.movie_one.id, self.movie_two.id])
        self.assertEqual(CollectionMovie.objects.filter(collection_id=dto.id).count(), 2)

    def test_retrieve_collection_enforces_private_visibility(self):
        dto = self.service.create_collection(
            owner=self.owner,
            name='Private',
            description='Just me',
            is_public=False,
            movie_ids=None,
        )

        with self.assertRaises(PermissionError):
            self.service.retrieve_collection(user=self.another_user, collection_id=dto.id)

        admin_view = self.service.retrieve_collection(user=self.admin, collection_id=dto.id)
        self.assertEqual(admin_view.id, dto.id)

    def test_list_collections_returns_public_conditionally(self):
        public_collection = self.service.create_collection(
            owner=self.owner,
            name='Public',
            description='Shareable',
            is_public=True,
            movie_ids=None,
        )
        private_collection = self.service.create_collection(
            owner=self.owner,
            name='Secret',
            description='Hidden',
            is_public=False,
            movie_ids=None,
        )

        anonymous_view = self.service.list_collections(user=None)
        self.assertEqual([collection.id for collection in anonymous_view.items], [public_collection.id])
        self.assertEqual(anonymous_view.total_count, 1)

        owner_default = self.service.list_collections(user=self.owner)
        self.assertEqual([collection.id for collection in owner_default.items], [public_collection.id])

        owned_only = self.service.list_collections(user=self.owner, owner_id=self.owner.id)
        self.assertEqual({collection.id for collection in owned_only.items}, {public_collection.id, private_collection.id})

        limited = self.service.list_collections(user=self.owner, owner_id=self.owner.id, limit=1, offset=1)
        self.assertEqual(limited.total_count, 2)
        self.assertEqual(len(limited.items), 1)

        other_user_owned = self.service.list_collections(user=self.another_user, owner_id=self.owner.id)
        self.assertEqual([collection.id for collection in other_user_owned.items], [public_collection.id])

        only_public = self.service.list_collections(user=self.owner, is_public=True)
        self.assertEqual([collection.id for collection in only_public.items], [public_collection.id])

    def test_update_collection_replaces_movies(self):
        dto = self.service.create_collection(
            owner=self.owner,
            name='Editable',
            description='Original',
            is_public=False,
            movie_ids=[self.movie_one.id],
        )

        updated = self.service.update_collection(
            user=self.owner,
            collection_id=dto.id,
            name='Updated',
            description='Changed',
            is_public=True,
            movie_ids=[self.movie_three.id],
        )

        self.assertEqual(updated.name, 'Updated')
        positions = list(CollectionMovie.objects.filter(collection_id=dto.id).values_list('movie_id', flat=True))
        self.assertEqual(positions, [self.movie_three.id])

    def test_delete_collection_requires_owner_or_admin(self):
        dto = self.service.create_collection(
            owner=self.owner,
            name='Disposable',
            description='',
            is_public=False,
            movie_ids=None,
        )

        with self.assertRaises(PermissionError):
            self.service.delete_collection(user=self.another_user, collection_id=dto.id)

        self.service.delete_collection(user=self.admin, collection_id=dto.id)
        self.assertFalse(Collection.objects.filter(pk=dto.id).exists())

    def test_retrieve_public_collection_allows_anonymous(self):
        dto = self.service.create_collection(
            owner=self.owner,
            name='Open',
            description='',
            is_public=True,
            movie_ids=None,
        )

        fetched = self.service.retrieve_collection(user=None, collection_id=dto.id)
        self.assertEqual(fetched.id, dto.id)

    def test_anonymous_users_cannot_edit(self):
        dto = self.service.create_collection(
            owner=self.owner,
            name='Locked',
            description='',
            is_public=False,
            movie_ids=None,
        )

        with self.assertRaises(PermissionError):
            self.service.update_collection(
                user=None,
                collection_id=dto.id,
                name='Nope',
            )

    def test_create_collection_validates_movie_ids(self):
        with self.assertRaises(ValidationError):
            self.service.create_collection(
                owner=self.owner,
                name='Broken',
                description='',
                is_public=False,
                movie_ids=[9999],
            )
