"""
Backfill imdb_rating and imdb_votes for movies that have imdb_id but empty rating.
Uses OMDb by id (?i=) to avoid creating duplicates. Rate-limited to respect API.
"""

import time

from django.core.management.base import BaseCommand

from movie.models import Movie
from movie.repositories import MovieRepository


class Command(BaseCommand):
    help = 'Backfill imdb_rating and imdb_votes for movies with imdb_id and empty imdb_rating (OMDb by id).'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delay',
            type=float,
            default=0.25,
            help='Seconds to wait between OMDb requests (default 0.25).',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Only list movies that would be updated, do not call OMDb.',
        )

    def handle(self, *args, **options):
        delay = options['delay']
        dry_run = options['dry_run']
        repo = MovieRepository()

        qs = Movie.objects.filter(imdb_id__isnull=False).exclude(imdb_id='')
        qs = qs.filter(imdb_rating='')
        movies = list(qs.values_list('id', 'imdb_id', 'title'))
        total = len(movies)

        if not movies:
            self.stdout.write(self.style.SUCCESS('No movies with empty imdb_rating found.'))
            return

        self.stdout.write(f'Found {total} movie(s) with empty imdb_rating.')
        if dry_run:
            for _id, imdb_id, title in movies[:20]:
                self.stdout.write(f'  {imdb_id}  {title}')
            if total > 20:
                self.stdout.write(f'  ... and {total - 20} more.')
            return

        updated = 0
        failed = 0
        for i, (pk, imdb_id, title) in enumerate(movies):
            if i > 0:
                time.sleep(delay)
            omdb = repo.get_movie_from_omdb_by_id(imdb_id)
            if omdb is None:
                failed += 1
                self.stdout.write(self.style.WARNING(f'  No OMDb data: {imdb_id}  {title}'))
                continue
            rating = (omdb.imdb_rating or '').strip()
            votes = (omdb.imdb_votes or '').strip()
            if not rating and not votes:
                continue
            Movie.objects.filter(pk=pk).update(imdb_rating=rating, imdb_votes=votes)
            updated += 1
            self.stdout.write(f'  Updated {imdb_id}: rating={rating!r} votes={votes!r}  {title}')

        self.stdout.write(self.style.SUCCESS(f'Done. Updated {updated}, no data {failed}, total processed {total}.'))
