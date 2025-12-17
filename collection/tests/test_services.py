from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from collection.models import Collection
from collection.repositories import CollectionRepository
from collection.services import CollectionService
from movie.models import Genre, Movie


class CollectionServiceTests(TestCase):
    def setUp(self):
        self.service = CollectionService()
        self.owner = get_user_model().objects.create_user(email='owner@example.com', password='pass1234')
        self.another_user = get_user_model().objects.create_user(email='another@example.com', password='pass1234')
        self.admin = get_user_model().objects.create_user(email='admin@example.com', password='pass1234', is_staff=True)

        self.movie_one = Movie.objects.create(title='Movie One', title_ua='Фільм Один', imdb_id='tt000010', poster='poster-1.jpg')
        self.movie_two = Movie.objects.create(title='Movie Two', title_ua='Фільм Два', imdb_id='tt000011', poster='poster-2.jpg')
        self.movie_three = Movie.objects.create(title='Movie Three', title_ua='Фільм Три', imdb_id='tt000012', poster='poster-3.jpg')

    def test_create_collection_with_movies(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Favorites',
            description='Top picks',
            design='grid',
            is_public=False,
            movie_ids=[self.movie_one.id, self.movie_two.id],
        )

        self.assertEqual(dto.owner_id, self.owner.id)
        self.assertEqual(dto.design, 'grid')
        self.assertEqual(dto.movies_count, 2)
        movies = self.service.list_collection_movies(viewer_id=self.owner.id, is_staff=False, collection_id=dto.id)
        self.assertEqual([movie.id for movie in movies.items], [self.movie_one.id, self.movie_two.id])

    def test_retrieve_collection_enforces_private_visibility(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Private',
            description='Just me',
            is_public=False,
            movie_ids=None,
        )

        with self.assertRaises(PermissionError):
            self.service.retrieve_collection(viewer_id=self.another_user.id, is_staff=False, collection_id=dto.id)

        admin_view = self.service.retrieve_collection(viewer_id=self.admin.id, is_staff=True, collection_id=dto.id)
        self.assertEqual(admin_view.id, dto.id)

    def test_list_collections_returns_public_conditionally(self):
        public_collection = self.service.create_collection(
            owner_id=self.owner.id,
            name='Public',
            description='Shareable',
            is_public=True,
            movie_ids=None,
        )
        private_collection = self.service.create_collection(
            owner_id=self.owner.id,
            name='Secret',
            description='Hidden',
            is_public=False,
            movie_ids=None,
        )

        another_view = self.service.list_collections(viewer_id=self.another_user.id, is_staff=False)
        self.assertEqual([collection.id for collection in another_view.items], [public_collection.id])
        self.assertEqual(another_view.total_count, 1)

        owner_default = self.service.list_collections(viewer_id=self.owner.id, is_staff=False)
        self.assertEqual([collection.id for collection in owner_default.items], [public_collection.id])

        owned_only = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, owner_id=self.owner.id)
        self.assertEqual({collection.id for collection in owned_only.items}, {public_collection.id, private_collection.id})

        limited = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, owner_id=self.owner.id, limit=1, offset=1)
        self.assertEqual(limited.total_count, 2)
        self.assertEqual(len(limited.items), 1)

        other_user_owned = self.service.list_collections(viewer_id=self.another_user.id, is_staff=False, owner_id=self.owner.id)
        self.assertEqual([collection.id for collection in other_user_owned.items], [public_collection.id])

        only_public = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, is_public=True)
        self.assertEqual([collection.id for collection in only_public.items], [public_collection.id])

    def test_list_collections_supports_search_and_ordering(self):
        alpha = self.service.create_collection(
            owner_id=self.owner.id,
            name='Alpha Picks',
            description='',
            is_public=True,
            movie_ids=None,
        )
        beta = self.service.create_collection(
            owner_id=self.owner.id,
            name='Beta Bag',
            description='',
            is_public=True,
            movie_ids=None,
        )
        extra_user = get_user_model().objects.create_user(email='extra@example.com', password='pass1234')
        self.service.subscribe(viewer_id=self.another_user.id, is_staff=False, collection_id=alpha.id)
        self.service.subscribe(viewer_id=extra_user.id, is_staff=False, collection_id=alpha.id)
        now = timezone.now()
        Collection.objects.filter(pk=alpha.id).update(created_at=now - timedelta(days=1))
        Collection.objects.filter(pk=beta.id).update(created_at=now)

        search_result = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, search='alpha')
        self.assertEqual([collection.id for collection in search_result.items], [alpha.id])
        self.assertEqual(search_result.items[0].subscribers_count, 2)

        ordering_result = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, ordering='-subscribers')
        self.assertEqual([collection.id for collection in ordering_result.items], [alpha.id, beta.id])

        created_at_order = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, ordering='created_at')
        self.assertEqual([collection.id for collection in created_at_order.items], [alpha.id, beta.id])

        blank_ordering = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, ordering=',')
        self.assertEqual({collection.id for collection in blank_ordering.items}, {alpha.id, beta.id})

        with self.assertRaises(ValidationError):
            self.service.list_collections(viewer_id=self.owner.id, is_staff=False, ordering='invalid')

    def test_list_collection_movies_includes_title_ua_and_search(self):
        collection = self.service.create_collection(
            owner_id=self.owner.id,
            name='UA Titles',
            description='',
            is_public=True,
            movie_ids=[self.movie_one.id, self.movie_two.id],
        )

        movies = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=collection.id,
            title_search='фільм',
        )

        self.assertEqual([item.id for item in movies.items], [self.movie_one.id, self.movie_two.id])
        self.assertEqual([item.title_ua for item in movies.items], ['Фільм Один', 'Фільм Два'])

    def test_list_collections_includes_preview_movies(self):
        movie_four = Movie.objects.create(title='Movie Four', imdb_id='tt000013', poster='poster-4.jpg')
        no_poster = Movie.objects.create(title='No Poster', imdb_id='tt000014', poster='')
        collection = self.service.create_collection(
            owner_id=self.owner.id,
            name='Previewed',
            description='',
            is_public=True,
            movie_ids=[no_poster.id, self.movie_three.id, self.movie_one.id, movie_four.id, self.movie_two.id],
        )

        result = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, owner_id=self.owner.id)
        self.assertEqual(len(result.items), 1)
        self.assertEqual(result.items[0].id, collection.id)
        preview = result.items[0].preview_movies
        self.assertEqual(len(preview), 3)
        self.assertEqual([movie.id for movie in preview], [self.movie_three.id, self.movie_one.id, movie_four.id])
        self.assertEqual(preview[0].title, 'Movie Three')
        self.assertEqual(preview[0].poster, 'poster-3.jpg')

    def test_preview_movies_populated_without_prefetch(self):
        collection = Collection.objects.create(owner=self.owner, name='No Prefetch', description='', is_public=True)
        CollectionMovie = collection.collection_movies.model  # type: ignore[attr-defined]
        no_poster = Movie.objects.create(title='Posterless', imdb_id='tt009999', poster='')
        CollectionMovie.objects.create(collection=collection, movie=no_poster, position=0)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_two, position=1)
        CollectionMovie.objects.create(collection=collection, movie=self.movie_one, position=2)

        fresh = Collection.objects.get(pk=collection.id)
        previews = CollectionRepository._build_preview_movies(fresh)

        self.assertEqual([movie.id for movie in previews], [self.movie_two.id, self.movie_one.id])

    def test_update_collection_replaces_movies(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Editable',
            description='Original',
            is_public=False,
            movie_ids=[self.movie_one.id],
        )

        updated = self.service.update_collection(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            name='Updated',
            description='Changed',
            design='list',
            is_public=True,
            movie_ids=[self.movie_three.id],
        )

        self.assertEqual(updated.name, 'Updated')
        self.assertEqual(updated.design, 'list')
        movies = self.service.list_collection_movies(viewer_id=self.owner.id, is_staff=False, collection_id=dto.id)
        self.assertEqual([movie.id for movie in movies.items], [self.movie_three.id])

    def test_delete_collection_requires_owner_or_admin(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Disposable',
            description='',
            is_public=False,
            movie_ids=None,
        )

        with self.assertRaises(PermissionError):
            self.service.delete_collection(viewer_id=self.another_user.id, is_staff=False, collection_id=dto.id)

        self.service.delete_collection(viewer_id=self.admin.id, is_staff=True, collection_id=dto.id)
        self.assertFalse(Collection.objects.filter(pk=dto.id).exists())

    def test_retrieve_public_collection_allows_anonymous(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Open',
            description='',
            is_public=True,
            movie_ids=None,
        )

        fetched = self.service.retrieve_collection(viewer_id=self.another_user.id, is_staff=False, collection_id=dto.id)
        self.assertEqual(fetched.id, dto.id)

    def test_anonymous_users_cannot_edit(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Locked',
            description='',
            is_public=False,
            movie_ids=None,
        )

        with self.assertRaises(PermissionError):
            self.service.update_collection(
                viewer_id=self.another_user.id,
                is_staff=False,
                collection_id=dto.id,
                name='Nope',
            )

    def test_create_collection_validates_movie_ids(self):
        with self.assertRaises(ValidationError):
            self.service.create_collection(
                owner_id=self.owner.id,
                name='Broken',
                description='',
                is_public=False,
                movie_ids=[9999],
            )

    def test_subscribe_and_filter_by_subscription(self):
        public_collection = self.service.create_collection(
            owner_id=self.owner.id,
            name='Public',
            description='',
            is_public=True,
            movie_ids=None,
        )
        other_public = self.service.create_collection(
            owner_id=self.owner.id,
            name='Other',
            description='',
            is_public=True,
            movie_ids=None,
        )
        self.service.subscribe(viewer_id=self.another_user.id, is_staff=False, collection_id=public_collection.id)

        subscribed = self.service.list_collections(viewer_id=self.another_user.id, is_staff=False, subscribed=True)
        self.assertEqual([collection.id for collection in subscribed.items], [public_collection.id])

        unsubscribed_view = self.service.list_collections(viewer_id=self.another_user.id, is_staff=False, subscribed=False)
        self.assertEqual({collection.id for collection in unsubscribed_view.items}, {other_public.id})

        all_collections = self.service.list_collections(viewer_id=self.another_user.id, is_staff=False, subscribed=None)
        self.assertEqual({collection.id for collection in all_collections.items}, {public_collection.id, other_public.id})

    def test_is_subscribed_flag_propagates(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Open',
            description='',
            is_public=True,
            movie_ids=None,
        )
        self.service.subscribe(viewer_id=self.another_user.id, is_staff=False, collection_id=dto.id)

        list_result = self.service.list_collections(viewer_id=self.another_user.id, is_staff=False)
        self.assertTrue(list_result.items[0].is_subscribed)

        detail = self.service.retrieve_collection(viewer_id=self.another_user.id, is_staff=False, collection_id=dto.id)
        self.assertTrue(detail.is_subscribed)

    def test_clone_collection_copies_movies_and_owner(self):
        source = self.service.create_collection(
            owner_id=self.owner.id,
            name='Clone Me',
            description='Desc',
            design='tiled',
            is_public=True,
            movie_ids=[self.movie_one.id, self.movie_two.id],
        )
        cloned = self.service.clone_collection(viewer_id=self.another_user.id, is_staff=False, collection_id=source.id)

        self.assertEqual(cloned.name, source.name)
        self.assertEqual(cloned.owner_id, self.another_user.id)
        self.assertEqual(cloned.design, 'tiled')
        movies = self.service.list_collection_movies(viewer_id=self.another_user.id, is_staff=False, collection_id=cloned.id)
        self.assertEqual([movie.id for movie in movies.items], [self.movie_one.id, self.movie_two.id])

    def test_clone_private_collection_requires_access(self):
        source = self.service.create_collection(
            owner_id=self.owner.id,
            name='Private Clone',
            description='',
            is_public=False,
            movie_ids=None,
        )
        with self.assertRaises(PermissionError):
            self.service.clone_collection(viewer_id=self.another_user.id, is_staff=False, collection_id=source.id)

    def test_clone_allows_same_name(self):
        source = self.service.create_collection(
            owner_id=self.owner.id,
            name='Original',
            description='',
            is_public=True,
            movie_ids=None,
        )
        existing = self.service.create_collection(
            owner_id=self.another_user.id,
            name='Original',
            description='',
            is_public=True,
            movie_ids=None,
        )
        cloned = self.service.clone_collection(viewer_id=self.another_user.id, is_staff=False, collection_id=source.id)

        self.assertEqual(cloned.name, source.name)
        self.assertNotEqual(cloned.id, existing.id)
        self.assertEqual(cloned.owner_id, self.another_user.id)

    def test_subscribe_noop_for_owner(self):
        collection = self.service.create_collection(
            owner_id=self.owner.id,
            name='Owner Collection',
            description='',
            is_public=True,
            movie_ids=None,
        )
        self.service.subscribe(viewer_id=self.owner.id, is_staff=False, collection_id=collection.id)
        refreshed = Collection.objects.get(pk=collection.id)
        self.assertFalse(refreshed.subscriptions.exists())

    def test_movies_count_not_multiplied_by_subscribers(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Counted',
            description='',
            is_public=True,
            movie_ids=[self.movie_one.id, self.movie_two.id, self.movie_three.id],
        )
        extra_user = get_user_model().objects.create_user(email='extra2@example.com', password='pass1234')
        self.service.subscribe(viewer_id=self.another_user.id, is_staff=False, collection_id=dto.id)
        self.service.subscribe(viewer_id=extra_user.id, is_staff=False, collection_id=dto.id)

        listed = self.service.list_collections(viewer_id=self.owner.id, is_staff=False, owner_id=self.owner.id)
        self.assertEqual(listed.items[0].movies_count, 3)
        detail = self.service.retrieve_collection(viewer_id=self.owner.id, is_staff=False, collection_id=dto.id)
        self.assertEqual(detail.movies_count, 3)

    def test_unsubscribe_requires_authentication(self):
        with self.assertRaises(TypeError):
            self.service.unsubscribe()  # type: ignore[arg-type]

    def test_clone_requires_authentication(self):
        with self.assertRaises(TypeError):
            self.service.clone_collection()  # type: ignore[arg-type]

    def test_list_collection_movies_supports_offset(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Offset',
            description='',
            is_public=True,
            movie_ids=[self.movie_one.id, self.movie_two.id],
        )
        movies = self.service.list_collection_movies(viewer_id=self.owner.id, is_staff=False, collection_id=dto.id, offset=1)
        self.assertEqual([movie.id for movie in movies.items], [self.movie_two.id])

    def test_list_collection_movies_supports_filters(self):
        dto = self.service.create_collection(
            owner_id=self.owner.id,
            name='Filters',
            description='',
            design='',
            is_public=True,
            movie_ids=[self.movie_one.id, self.movie_two.id, self.movie_three.id],
        )
        thriller = Genre.objects.create(name='Thriller')
        Movie.objects.filter(pk=self.movie_one.id).update(title='Alpha', imdb_rating='6.5', year='2020')
        Movie.objects.filter(pk=self.movie_two.id).update(title='Beta Filter', imdb_rating='8.2', year='2021')
        Movie.objects.filter(pk=self.movie_three.id).update(title='Gamma', imdb_rating='7.1', year='2019')
        refreshed_two = Movie.objects.get(pk=self.movie_two.id)
        refreshed_two.genres.add(thriller)

        filtered = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            title_search='Filter',
            rating_min=8.0,
        )
        self.assertEqual([movie.id for movie in filtered.items], [self.movie_two.id])
        self.assertIsNotNone(filtered.items[0].description)

        genre_filtered = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            genres='Thrill',
        )
        self.assertEqual([movie.id for movie in genre_filtered.items], [self.movie_two.id])

        year_filtered = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            year='2021',
        )
        self.assertEqual([movie.id for movie in year_filtered.items], [self.movie_two.id])

        imdb_filtered = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            imdb_id=refreshed_two.imdb_id,
            rating_max=9.0,
        )
        self.assertEqual([movie.id for movie in imdb_filtered.items], [self.movie_two.id])

        ordered = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            ordering='-year',
        )
        self.assertEqual([movie.year for movie in ordered.items], ['2021', '2020', '2019'])

        rating_ordered = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            ordering='-imdb_rating',
        )
        self.assertEqual(
            [movie.imdb_id for movie in rating_ordered.items],
            [self.movie_two.imdb_id, self.movie_three.imdb_id, self.movie_one.imdb_id],
        )

        fallback_ordering = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            ordering='',
        )
        self.assertEqual([movie.id for movie in fallback_ordering.items], [self.movie_one.id, self.movie_two.id, self.movie_three.id])

        comma_ordering = self.service.list_collection_movies(
            viewer_id=self.owner.id,
            is_staff=False,
            collection_id=dto.id,
            ordering=',',
        )
        self.assertEqual([movie.id for movie in comma_ordering.items], [self.movie_one.id, self.movie_two.id, self.movie_three.id])
