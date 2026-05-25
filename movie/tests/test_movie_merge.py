from django.test import SimpleTestCase

from movie.dataclasses import Actor, Director, Genre, OmdbMovie, Rating
from movie.movie_merge import merge_omdb_with_tmdb_fallback


class MergeOmdbWithTmdbFallbackTests(SimpleTestCase):
    def test_keeps_omdb_ratings_and_poster(self):
        omdb_movie = OmdbMovie(
            title='The Matrix',
            imdb_id='tt0133093',
            imdb_rating='8.7',
            imdb_votes='1,900,000',
            metascore='73',
            awards='Won 4 Oscars',
            poster='https://example.com/omdb.jpg',
            plot='OMDb plot',
            genres=[Genre(name='Action')],
        )
        tmdb_movie = OmdbMovie(
            title='The Matrix',
            imdb_id='tt0133093',
            imdb_rating='8.2',
            poster='https://image.tmdb.org/t/p/w500/tmdb.jpg',
            plot='TMDB plot',
            ratings=[Rating(source='TMDB', value='8.2/10')],
        )

        merged = merge_omdb_with_tmdb_fallback(omdb_movie, tmdb_movie)

        self.assertEqual(merged.imdb_rating, '8.7')
        self.assertEqual(merged.metascore, '73')
        self.assertEqual(merged.awards, 'Won 4 Oscars')
        self.assertEqual(merged.poster, 'https://example.com/omdb.jpg')
        self.assertEqual(merged.plot, 'OMDb plot')
        self.assertEqual(len(merged.ratings), 1)
        self.assertEqual(merged.ratings[0].source, 'TMDB')

    def test_fills_missing_poster_and_plot_from_tmdb(self):
        omdb_movie = OmdbMovie(
            title='Inception',
            imdb_id='tt1375666',
            imdb_rating='8.8',
            poster='N/A',
            plot=None,
            genres=[Genre(name='Sci-Fi')],
        )
        tmdb_movie = OmdbMovie(
            title='Inception',
            imdb_id='tt1375666',
            poster='https://image.tmdb.org/t/p/w500/inception.jpg',
            plot='A thief who steals secrets through dreams.',
            directors=[Director(full_name='Christopher Nolan')],
            ratings=[Rating(source='TMDB', value='8.4/10')],
        )

        merged = merge_omdb_with_tmdb_fallback(omdb_movie, tmdb_movie)

        self.assertEqual(merged.poster, 'https://image.tmdb.org/t/p/w500/inception.jpg')
        self.assertEqual(merged.plot, 'A thief who steals secrets through dreams.')
        self.assertEqual(merged.imdb_rating, '8.8')
        self.assertEqual(merged.directors[0].full_name, 'Christopher Nolan')

    def test_appends_missing_cast_from_tmdb(self):
        omdb_movie = OmdbMovie(
            title='Interstellar',
            imdb_id='tt0816692',
            actors=[Actor(full_name='Matthew McConaughey')],
            genres=[Genre(name='Adventure')],
        )
        tmdb_movie = OmdbMovie(
            title='Interstellar',
            imdb_id='tt0816692',
            actors=[
                Actor(full_name='Matthew McConaughey'),
                Actor(full_name='Anne Hathaway'),
            ],
            genres=[Genre(name='Adventure')],
        )

        merged = merge_omdb_with_tmdb_fallback(omdb_movie, tmdb_movie)
        names = {actor.full_name for actor in merged.actors}
        self.assertEqual(names, {'Matthew McConaughey', 'Anne Hathaway'})
