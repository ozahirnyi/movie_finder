from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from collection.models import Collection, CollectionMovie
from collection.views import CollectionListCreateView, CollectionMoviesView
from movie.models import Movie


class CollectionViewTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='user@example.com', password='pass1234')
        self.other_user = get_user_model().objects.create_user(email='other@example.com', password='pass1234')
        self.admin = get_user_model().objects.create_user(email='admin@example.com', password='pass1234', is_staff=True)
        self.movie_one = Movie.objects.create(title='Movie One', imdb_id='tt010001')
        self.movie_two = Movie.objects.create(title='Movie Two', imdb_id='tt010002')

    def test_create_collection(self):
        self.client.force_authenticate(user=self.user)
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
        self.assertEqual(response.data['movies_count'], 2)
        self.assertNotIn('movies', response.data)
        self.assertTrue(Collection.objects.filter(name='Weekend Watch', owner=self.user).exists())

    def test_update_collection_requires_owner_or_admin(self):
        collection = Collection.objects.create(owner=self.user, name='Private', description='', is_public=False)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_one)

        self.client.force_authenticate(user=self.other_user)
        response = self.client.patch(
            reverse('collection_detail', kwargs={'collection_id': collection.id}),
            data={'name': 'Hack'},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.admin)
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

        self.client.force_authenticate(user=self.user)
        owner_response = self.client.get(reverse('collections'))
        self.assertEqual(len(owner_response.data['results']), 1)
        self.assertEqual(owner_response.data['results'][0]['name'], 'Public')

    def test_list_collections_supports_filters(self):
        public = Collection.objects.create(owner=self.user, name='Public Filter', description='', is_public=True)
        private = Collection.objects.create(owner=self.user, name='Private Filter', description='', is_public=False)
        self.client.force_authenticate(user=self.user)

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
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('collections'), {'owner_id': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('owner_id', response.data)

    def test_private_collection_not_accessible_without_auth(self):
        collection = Collection.objects.create(owner=self.user, name='Secret', description='', is_public=False)

        self.client.force_authenticate(user=self.user)
        authorized = self.client.get(reverse('collection_detail', kwargs={'collection_id': collection.id}))
        self.assertEqual(authorized.status_code, status.HTTP_200_OK)

    def test_delete_collection(self):
        collection = Collection.objects.create(owner=self.user, name='Disposable', description='', is_public=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse('collection_detail', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Collection.objects.filter(pk=collection.id).exists())

    def test_delete_collection_forbidden_for_non_owner(self):
        collection = Collection.objects.create(owner=self.user, name='Protected', description='', is_public=False)
        self.client.force_authenticate(user=self.other_user)

        response = self.client.delete(reverse('collection_detail', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Collection.objects.filter(pk=collection.id).exists())

    def test_private_collection_forbidden_for_non_owner(self):
        collection = Collection.objects.create(owner=self.other_user, name='Protected', description='', is_public=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('collection_detail', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_collections_ignores_invalid_boolean_filter(self):
        Collection.objects.create(owner=self.user, name='One', description='', is_public=True)
        Collection.objects.create(owner=self.user, name='Two', description='', is_public=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('collections'), {'is_public': 'maybe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'One')

    def test_list_without_pagination_returns_plain_response(self):
        original_pagination = CollectionListCreateView.pagination_class
        CollectionListCreateView.pagination_class = None
        self.addCleanup(lambda: setattr(CollectionListCreateView, 'pagination_class', original_pagination))

        Collection.objects.create(owner=self.user, name='No Pagination', description='', is_public=True)
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('collections'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)

    def test_owner_id_controls_visibility(self):
        Collection.objects.create(owner=self.user, name='Public', description='', is_public=True)
        Collection.objects.create(owner=self.user, name='Private', description='', is_public=False)

        self.client.force_authenticate(user=self.user)
        owner_response = self.client.get(reverse('collections'), {'owner_id': str(self.user.id)})
        returned_names = {item['name'] for item in owner_response.data['results']}
        self.assertEqual(returned_names, {'Public', 'Private'})

        self.client.force_authenticate(user=self.other_user)
        other_response = self.client.get(reverse('collections'), {'owner_id': str(self.user.id)})
        self.assertEqual(len(other_response.data['results']), 1)
        self.assertEqual(other_response.data['results'][0]['name'], 'Public')

    def test_subscription_filter_requires_authentication(self):
        Collection.objects.create(owner=self.user, name='Public', description='', is_public=True)
        response = self.client.get(reverse('collections'), {'subscribed': 'true'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_subscribe_and_unsubscribe_endpoints(self):
        collection = Collection.objects.create(owner=self.other_user, name='Shareable', description='', is_public=True)

        self.client.force_authenticate(user=self.user)
        subscribe_response = self.client.post(reverse('collection_subscribe', kwargs={'collection_id': collection.id}))
        self.assertEqual(subscribe_response.status_code, status.HTTP_204_NO_CONTENT)

        list_response = self.client.get(reverse('collections'))
        self.assertTrue(list_response.data['results'][0]['is_subscribed'])

        unsubscribe_response = self.client.delete(reverse('collection_subscribe', kwargs={'collection_id': collection.id}))
        self.assertEqual(unsubscribe_response.status_code, status.HTTP_204_NO_CONTENT)
        refreshed = self.client.get(reverse('collections'))
        self.assertFalse(refreshed.data['results'][0]['is_subscribed'])

    def test_subscribed_filter_returns_only_subscribed(self):
        public = Collection.objects.create(owner=self.other_user, name='Public', description='', is_public=True)
        other = Collection.objects.create(owner=self.other_user, name='Other', description='', is_public=True)

        self.client.force_authenticate(user=self.user)
        self.client.post(reverse('collection_subscribe', kwargs={'collection_id': public.id}))

        subscribed = self.client.get(reverse('collections'), {'subscribed': 'true'})
        self.assertEqual([item['id'] for item in subscribed.data['results']], [public.id])

        unsubscribed = self.client.get(reverse('collections'), {'subscribed': 'false'})
        returned_ids = {item['id'] for item in unsubscribed.data['results']}
        self.assertEqual(returned_ids, {other.id})

        all_collections = self.client.get(reverse('collections'))
        all_ids = {item['id'] for item in all_collections.data['results']}
        self.assertEqual(all_ids, {public.id, other.id})

    def test_collection_movies_endpoint(self):
        collection = Collection.objects.create(owner=self.user, name='With Movies', description='', is_public=True)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_one, position=0)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_two, position=1)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('collection_movies', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([movie['id'] for movie in response.data['results']], [self.movie_one.id, self.movie_two.id])

    def test_collection_movies_private_requires_access(self):
        collection = Collection.objects.create(owner=self.other_user, name='Hidden', description='', is_public=False)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_one, position=0)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('collection_movies', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.other_user)
        authorized = self.client.get(reverse('collection_movies', kwargs={'collection_id': collection.id}))
        self.assertEqual(authorized.status_code, status.HTTP_200_OK)

    def test_collection_movies_without_pagination(self):
        original_pagination = CollectionMoviesView.pagination_class
        CollectionMoviesView.pagination_class = None
        self.addCleanup(lambda: setattr(CollectionMoviesView, 'pagination_class', original_pagination))

        collection = Collection.objects.create(owner=self.user, name='NoPag', description='', is_public=True)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_one, position=0)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_two, position=1)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('collection_movies', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)

    def test_clone_collection_endpoint(self):
        source = Collection.objects.create(owner=self.other_user, name='Source', description='OG', is_public=True)
        CollectionMovie.objects.create(collection=source, movie=self.movie_one, position=0)
        self.client.force_authenticate(user=self.user)

        clone_response = self.client.post(reverse('collection_clone', kwargs={'collection_id': source.id}))
        self.assertEqual(clone_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(clone_response.data['name'], 'Source')
        self.assertEqual(clone_response.data['owner_id'], self.user.id)
        self.assertEqual(clone_response.data['movies_count'], 1)

        movies_response = self.client.get(reverse('collection_movies', kwargs={'collection_id': clone_response.data['id']}))
        self.assertEqual([movie['id'] for movie in movies_response.data['results']], [self.movie_one.id])

    def test_clone_private_collection_forbidden(self):
        source = Collection.objects.create(owner=self.other_user, name='Hidden Source', description='', is_public=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.post(reverse('collection_clone', kwargs={'collection_id': source.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_clone_conflict_same_name(self):
        source = Collection.objects.create(owner=self.other_user, name='Repeat', description='', is_public=True)
        Collection.objects.create(owner=self.user, name='Repeat', description='', is_public=True)
        self.client.force_authenticate(user=self.user)

        response = self.client.post(reverse('collection_clone', kwargs={'collection_id': source.id}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_subscribe_private_collection_forbidden(self):
        collection = Collection.objects.create(owner=self.other_user, name='Hidden', description='', is_public=False)

        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('collection_subscribe', kwargs={'collection_id': collection.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
