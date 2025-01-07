from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .dataclasses import AiMovie, ImdbMovie
from .errors import AddLikeError
from .models import Movie, WatchLaterMovie, LikeMovie


class FinderTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(title="test", imdb_id="1")

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="neo@neo.neo", password="neoneoneo")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_get_movie(self):
        with self.assertNumQueries(2):
            response = self.client.get(reverse("movie", kwargs={"id": self.movie.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_like_movie(self):
        self.client.force_login(self.user)
        with self.assertNumQueries(2):
            response = self.client.post(
                reverse("movie_like", kwargs={"id": self.movie.id})
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_like_movie_error(self):
        self.client.force_login(self.user)
        with self.assertNumQueries(2):
            response = self.client.post(
                reverse("movie_like", kwargs={"id": self.movie.id})
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        with self.assertNumQueries(2):
            response = self.client.post(
                reverse("movie_like", kwargs={"id": self.movie.id})
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        default_code = response.data["detail"].code
        default_detail = response.data["detail"]
        self.assertEqual(default_code, AddLikeError.default_code)
        self.assertEqual(default_detail, AddLikeError.default_detail)

    def test_unlike_movie(self):
        LikeMovie.objects.create(user=self.user, movie=self.movie)
        self.client.force_login(self.user)
        with self.assertNumQueries(2):
            response = self.client.post(
                reverse("movie_unlike", kwargs={"id": self.movie.id})
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_find_movie(self):
        # TODO: uncomment when start use postgresql. > movie_finder_django/movie/models.py
        # with self.assertNumQueries(3):
        response = self.client.get(
            reverse("find_movie", kwargs={"expression": "Shrek"}) + '?test=1'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_watch_later(self):
        self.client.force_login(self.user)
        with self.assertNumQueries(3):
            response = self.client.post(
                reverse("watch_later_create"), data={"movie": self.movie.imdb_id}
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        wl = WatchLaterMovie.objects.filter(user=self.user, movie=self.movie)
        self.assertTrue(wl.exists())

    def test_delete_watch_later(self):
        wl = WatchLaterMovie.objects.create(user=self.user, movie=self.movie)

        self.client.force_login(self.user)
        with self.assertNumQueries(3):
            response = self.client.delete(
                reverse("watch_later_destroy", kwargs={"pk": wl.id})
            )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        wl = WatchLaterMovie.objects.filter(user=self.user, movie=self.movie)
        self.assertFalse(wl.exists())

    def test_get_watch_later(self):
        wrong_user = get_user_model().objects.create_user(email="notneo@neo.neo", password="neoneoneo")
        WatchLaterMovie.objects.create(user_id=wrong_user.id, movie_id=self.movie.id)
        WatchLaterMovie.objects.create(user_id=self.user.id, movie_id=self.movie.id)

        self.client.force_login(self.user)
        with self.assertNumQueries(3):
            response = self.client.get(reverse("watch_later_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data["results"][0]
        self.assertTrue(response_data["is_watch_later"])
        self.assertEqual(response_data["watch_later_count"], 2)


class FindMovieAiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email="neo@neo.neo", password="neoneoneo")
        self.client.force_login(self.user)

    @patch('movie.ai_find_movie.FindMovieAiClient.find_movies')
    @patch('movie.services.MovieService.get_movies_from_imdb')
    def test_find_movie_ai(self, mock_get_movies_from_imdb, mock_find_movies):
        mock_find_movies.return_value = [
            AiMovie(title="Shrek", genre="Animation", plot="A green ogre saves a princess."),
            AiMovie(title="Shrek 2", genre="Animation", plot="The ogre meets his in-laws."),
        ]

        def mock_get_movies(title):
            movies = {
                "Shrek": ImdbMovie(
                    title="Shrek", imdb_id="12345", poster="http://poster.url",
                    year="2001", type="movie"
                ),
                "Shrek 2": ImdbMovie(
                    title="Shrek 2", imdb_id="67890", poster="http://poster.url",
                    year="2004", type="movie"
                ),
            }
            return [movies.get(title)] if title in movies else []

        mock_get_movies_from_imdb.side_effect = mock_get_movies

        response = self.client.post(
            reverse("find_movie_ai"),
            data={"prompt": "Shrek"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        movie = response.data[0]
        self.assertEqual(movie["title"], "Shrek")
        self.assertEqual(movie["genre"], "Animation")
        self.assertEqual(movie["plot"], "A green ogre saves a princess.")
        self.assertEqual(movie["imdb_id"], "12345")

        self.assertTrue(Movie.objects.filter(title="Shrek").exists())

    def test_prompt_max_length(self):
        max_length = 255
        valid_prompt = "A" * max_length
        invalid_prompt = "A" * (max_length + 1)

        response = self.client.post(
            reverse("find_movie_ai"),
            data={"prompt": valid_prompt},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Valid prompt length should pass.")

        response = self.client.post(
            reverse("find_movie_ai"),
            data={"prompt": invalid_prompt},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "Invalid prompt length should fail.")
