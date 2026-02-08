"""
Load curated collections and movies from collection/curated_collections_seed.json.
Idempotent (get_or_create). Use on prod when migration 0006 already ran but seed did not apply.
"""

import json
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Count

from auth_app.models import User
from collection.models import Collection, CollectionMovie
from movie.models import Movie

# Empty curated collections from migration 0005 (Ukrainian names). Remove them so only English ones with movies remain.
CURATED_UKRAINIAN_NAMES = frozenset(
    {
        'Новорічна',
        'Хорор',
        'Комедія',
        'Драма',
        'Бойовик',
        'Романтика',
        'Фантастика',
        'Документальні',
        'Аніме',
        'Класика',
        'Для всієї родини',
        'Топ IMDb',
    }
)


def load_seed_data():
    path = Path(__file__).resolve().parent.parent.parent / 'curated_collections_seed.json'
    if not path.exists():
        return {'collections': []}
    return json.loads(path.read_text(encoding='utf-8'))


class Command(BaseCommand):
    help = 'Load curated collections and movies from curated_collections_seed.json (idempotent)'

    def handle(self, *args, **options):
        owner = User.objects.filter(is_superuser=True).first() or User.objects.first()
        if not owner:
            self.stderr.write(self.style.ERROR('No user in DB. Create a user first.'))
            return

        data = load_seed_data()
        if not data.get('collections'):
            self.stderr.write(self.style.WARNING('No collections in seed file or file missing.'))
            return

        with transaction.atomic():
            for coll_data in data.get('collections', []):
                name = coll_data.get('name', '')
                description = coll_data.get('description', '')
                design = (coll_data.get('design') or '').strip()
                coll, created = Collection.objects.get_or_create(
                    owner=owner,
                    name=name,
                    defaults={
                        'description': description,
                        'is_public': True,
                        'design': design,
                    },
                )
                if not created and design and coll.design != design:
                    coll.design = design
                    coll.save(update_fields=['design'])
                n_movies = 0
                for m in coll_data.get('movies', []):
                    imdb_id = (m.get('imdb_id') or '').strip()
                    if not imdb_id:
                        continue
                    movie, _ = Movie.objects.get_or_create(
                        imdb_id=imdb_id,
                        defaults={
                            'title': m.get('title', '') or '',
                            'year': m.get('year', '') or '',
                            'type': m.get('type', '') or 'movie',
                            'poster': m.get('poster', '') or '',
                            'plot': m.get('plot', '') or '',
                        },
                    )
                    CollectionMovie.objects.get_or_create(
                        collection=coll,
                        movie=movie,
                        defaults={'position': m.get('position', 0)},
                    )
                    n_movies += 1
                self.stdout.write(f'{name}: {n_movies} movies')
            # Remove empty Ukrainian-named collections from 0005 so only English ones with movies remain.
            empty_ukrainian = (
                Collection.objects.filter(owner=owner, name__in=CURATED_UKRAINIAN_NAMES)
                .annotate(n_movies=Count('collection_movies'))
                .filter(n_movies=0)
            )
            deleted = empty_ukrainian.count()
            empty_ukrainian.delete()
            if deleted:
                self.stdout.write(f'Removed {deleted} empty Ukrainian-named collection(s).')
        self.stdout.write(self.style.SUCCESS('Done.'))
