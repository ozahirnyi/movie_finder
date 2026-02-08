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
