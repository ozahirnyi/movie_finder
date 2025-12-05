from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class TopMovieAdminTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(email='admin@test.test', password='admintestpass')
        self.client.force_login(self.admin_user)

    def test_refresh_top_movies_action(self):
        with patch('movie.admin.TopMoviesService.force_refresh', return_value=['first', 'second']) as mock_refresh:
            response = self.client.get(reverse('admin:movie_topmovie_refresh'))

        self.assertEqual(response.status_code, 302)
        mock_refresh.assert_called_once_with()
