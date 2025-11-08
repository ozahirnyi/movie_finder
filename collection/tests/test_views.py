from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from collection.models import Collection, CollectionMovie
from collection.views import CollectionListCreateView
from movie.models import Movie


def _issue_jwt(client, user):
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')


class CollectionViewTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='user@example.com', password='pass1234')
        self.other_user = get_user_model().objects.create_user(email='other@example.com', password='pass1234')
        self.admin = get_user_model().objects.create_user(email='admin@example.com', password='pass1234', is_staff=True)
        self.movie_one = Movie.objects.create(title='Movie One', imdb_id='tt010001')
        self.movie_two = Movie.objects.create(title='Movie Two', imdb_id='tt010002')

    def test_create_collection(self):
        _issue_jwt(self.client, self.user)
        response = self.client.post(
            reverse('collections'),
            data={
                'name': 'Weekend Watch',
                'description': 'Good stuff',
                'is_public': True,
                'movie_ids': [self.movie_one.id, self.movie_two.id],
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Weekend Watch')
        self.assertEqual(len(response.data['movies']), 2)
        self.assertTrue(Collection.objects.filter(name='Weekend Watch', owner=self.user).exists())

    def test_update_collection_requires_owner_or_admin(self):
        collection = Collection.objects.create(owner=self.user, name='Private', description='', is_public=False)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_one)

        _issue_jwt(self.client, self.other_user)
        response = self.client.patch(
            reverse('collection_detail', kwargs={'collection_id': collection.id}),
            data={'name': 'Hack'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        _issue_jwt(self.client, self.admin)
        response = self.client.patch(
            reverse('collection_detail', kwargs={'collection_id': collection.id}),
            data={'name': 'Admin Edit'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        collection.refresh_from_db()
        self.assertEqual(collection.name, 'Admin Edit')

    def test_list_collections_filters_visibility(self):
        Collection.objects.create(owner=self.user, name='Public', description='', is_public=True)
        Collection.objects.create(owner=self.user, name='Private', description='', is_public=False)

        anonymous_response = self.client.get(reverse('collections'))
        self.assertEqual(anonymous_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(anonymous_response.data['results']), 1)
        self.assertEqual(anonymous_response.data['results'][0]['name'], 'Public')

        _issue_jwt(self.client, self.user)
        owner_response = self.client.get(reverse('collections'))
        self.assertEqual(len(owner_response.data['results']), 1)
        self.assertEqual(owner_response.data['results'][0]['name'], 'Public')

    def test_list_collections_supports_filters(self):
        public = Collection.objects.create(owner=self.user, name='Public Filter', description='', is_public=True)
        private = Collection.objects.create(owner=self.user, name='Private Filter', description='', is_public=False)
        _issue_jwt(self.client, self.user)

        public_response = self.client.get(reverse('collections'), {'is_public': 'true'})
        self.assertEqual(public_response.status_code, status.HTTP_200_OK)
        self.assertEqual([item['id'] for item in public_response.data['results']], [public.id])

        private_response = self.client.get(
            reverse('collections'),
            {'is_public': 'false', 'owner_id': str(self.user.id)},
        )
        self.assertEqual(private_response.status_code, status.HTTP_200_OK)
        self.assertEqual([item['id'] for item in private_response.data['results']], [private.id])

    def test_list_collections_invalid_owner_id(self):
        _issue_jwt(self.client, self.user)
        response = self.client.get(reverse('collections'), {'owner_id': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('owner_id', response.data)

    def test_private_collection_not_accessible_without_auth(self):
        collection = Collection.objects.create(owner=self.user, name='Secret', description='', is_public=False)

        response = self.client.get(reverse('collection_detail', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        _issue_jwt(self.client, self.user)
        authorized = self.client.get(reverse('collection_detail', kwargs={'collection_id': collection.id}))
        self.assertEqual(authorized.status_code, status.HTTP_200_OK)

    def test_delete_collection(self):
        collection = Collection.objects.create(owner=self.user, name='Disposable', description='', is_public=False)
        _issue_jwt(self.client, self.user)

        response = self.client.delete(reverse('collection_detail', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Collection.objects.filter(pk=collection.id).exists())

    def test_delete_collection_forbidden_for_non_owner(self):
        collection = Collection.objects.create(owner=self.user, name='Protected', description='', is_public=False)
        _issue_jwt(self.client, self.other_user)

        response = self.client.delete(reverse('collection_detail', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Collection.objects.filter(pk=collection.id).exists())

    def test_list_without_pagination_returns_plain_response(self):
        original_pagination = CollectionListCreateView.pagination_class
        CollectionListCreateView.pagination_class = None
        self.addCleanup(lambda: setattr(CollectionListCreateView, 'pagination_class', original_pagination))

        Collection.objects.create(owner=self.user, name='No Pagination', description='', is_public=True)

        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)

    def test_list_collections_ignores_invalid_boolean_filter(self):
        Collection.objects.create(owner=self.user, name='One', description='', is_public=True)
        Collection.objects.create(owner=self.user, name='Two', description='', is_public=False)
        _issue_jwt(self.client, self.user)

        response = self.client.get(reverse('collections'), {'is_public': 'maybe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'One')

    def test_owner_id_controls_visibility(self):
        Collection.objects.create(owner=self.user, name='Public', description='', is_public=True)
        Collection.objects.create(owner=self.user, name='Private', description='', is_public=False)

        _issue_jwt(self.client, self.user)
        owner_response = self.client.get(reverse('collections'), {'owner_id': str(self.user.id)})
        returned_names = {item['name'] for item in owner_response.data['results']}
        self.assertEqual(returned_names, {'Public', 'Private'})

        self.client.credentials()
        _issue_jwt(self.client, self.other_user)
        other_response = self.client.get(reverse('collections'), {'owner_id': str(self.user.id)})
        self.assertEqual(len(other_response.data['results']), 1)
        self.assertEqual(other_response.data['results'][0]['name'], 'Public')
