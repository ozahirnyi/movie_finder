from io import StringIO
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase

from movie.models import Movie


class BackfillMovieRatingsCommandTests(TestCase):
    def test_dry_run_lists_movies_with_empty_rating(self):
        Movie.objects.create(
            imdb_id='tt0126029',
            title='Shrek',
            year='2001',
            imdb_rating='',
            imdb_votes='',
        )
        out = StringIO()
        call_command('backfill_movie_ratings', '--dry-run', stdout=out)
        self.assertIn('1 movie(s)', out.getvalue())
        self.assertIn('tt0126029', out.getvalue())
        self.assertIn('Shrek', out.getvalue())
        movie = Movie.objects.get(imdb_id='tt0126029')
        self.assertEqual(movie.imdb_rating, '')

    def test_skips_when_no_movies_with_empty_rating(self):
        Movie.objects.create(
            imdb_id='tt0126029',
            title='Shrek',
            year='2001',
            imdb_rating='7.5',
            imdb_votes='500000',
        )
        out = StringIO()
        call_command('backfill_movie_ratings', stdout=out)
        self.assertIn('No movies with empty imdb_rating', out.getvalue())

    def test_dry_run_with_many_movies_truncates_output(self):
        for i in range(25):
            Movie.objects.create(
                imdb_id=f'tt{i:07d}',
                title=f'Movie {i}',
                year='2000',
                imdb_rating='',
                imdb_votes='',
            )
        out = StringIO()
        call_command('backfill_movie_ratings', '--dry-run', stdout=out)
        self.assertIn('25 movie(s)', out.getvalue())
        self.assertIn('... and 5 more.', out.getvalue())

    def test_backfill_handles_omdb_no_data(self):
        Movie.objects.create(
            imdb_id='tt9999999',
            title='Unknown',
            year='2000',
            imdb_rating='',
            imdb_votes='',
        )
        with patch('movie.repositories.requests.get') as mock_get:
            mock_get.return_value.json.return_value = {
                'Response': 'False',
                'Error': 'Movie not found!',
            }
            mock_get.return_value.raise_for_status = lambda: None
            out = StringIO()
            call_command('backfill_movie_ratings', '--delay=0', stdout=out)
        self.assertIn('No OMDb data', out.getvalue())
        movie = Movie.objects.get(imdb_id='tt9999999')
        self.assertEqual(movie.imdb_rating, '')

    def test_backfill_skips_when_rating_and_votes_empty(self):
        Movie.objects.create(
            imdb_id='tt0126029',
            title='Shrek',
            year='2001',
            imdb_rating='',
            imdb_votes='',
        )
        with patch('movie.repositories.requests.get') as mock_get:
            mock_get.return_value.json.return_value = {
                'Title': 'Shrek',
                'Year': '2001',
                'imdbID': 'tt0126029',
                'imdbRating': '',
                'imdbVotes': '',
                'Response': 'True',
                'Released': '18 May 2001',
                'Genre': 'Animation',
                'Director': 'Andrew Adamson',
                'Writer': 'Ted Elliott',
                'Actors': 'Mike Myers',
                'Plot': 'A plot',
                'Language': 'English',
                'Country': 'USA',
                'Poster': 'http://',
                'Type': 'movie',
                'Ratings': [],
            }
            mock_get.return_value.raise_for_status = lambda: None
            out = StringIO()
            call_command('backfill_movie_ratings', '--delay=0', stdout=out)
        movie = Movie.objects.get(imdb_id='tt0126029')
        self.assertEqual(movie.imdb_rating, '')

    def test_backfill_updates_rating_when_omdb_returns_data(self):
        movie = Movie.objects.create(
            imdb_id='tt0126029',
            title='Shrek',
            year='2001',
            imdb_rating='',
            imdb_votes='',
        )
        with patch('movie.repositories.requests.get') as mock_get:
            mock_get.return_value.json.return_value = {
                'Title': 'Shrek',
                'Year': '2001',
                'imdbID': 'tt0126029',
                'imdbRating': '7.5',
                'imdbVotes': '500,000',
                'Response': 'True',
                'Released': '18 May 2001',
                'Genre': 'Animation, Adventure, Comedy',
                'Director': 'Andrew Adamson, Vicky Jenson',
                'Writer': 'Ted Elliott',
                'Actors': 'Mike Myers',
                'Plot': 'A plot',
                'Language': 'English',
                'Country': 'USA',
                'Poster': 'http://',
                'Type': 'movie',
                'Ratings': [],
            }
            mock_get.return_value.raise_for_status = lambda: None
            out = StringIO()
            call_command('backfill_movie_ratings', '--delay=0', stdout=out)

        movie.refresh_from_db()
        self.assertEqual(movie.imdb_rating, '7.5')
        self.assertEqual(movie.imdb_votes, '500,000')

    @patch('movie.management.commands.backfill_movie_ratings.time.sleep')
    def test_backfill_uses_delay_between_requests(self, mock_sleep):
        for i in range(2):
            Movie.objects.create(
                imdb_id=f'tt{i:07d}',
                title=f'Movie {i}',
                year='2000',
                imdb_rating='',
                imdb_votes='',
            )
        base = {
            'Title': 'Movie',
            'Year': '2000',
            'imdbRating': '8.0',
            'imdbVotes': '1000',
            'Response': 'True',
            'Released': '01 Jan 2000',
            'Genre': 'Drama',
            'Director': 'Director',
            'Writer': 'Writer',
            'Actors': 'Actor',
            'Plot': 'Plot',
            'Language': 'English',
            'Country': 'USA',
            'Poster': '',
            'Type': 'movie',
            'Ratings': [],
        }
        responses = [{**base, 'imdbID': f'tt{i:07d}'} for i in range(2)]
        with patch('movie.repositories.requests.get') as mock_get:
            mock_get.return_value.json.side_effect = responses
            mock_get.return_value.raise_for_status = lambda: None
            call_command('backfill_movie_ratings', '--delay=0.5', stdout=StringIO())
        mock_sleep.assert_called_once_with(0.5)
