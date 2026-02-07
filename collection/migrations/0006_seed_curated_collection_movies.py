# Data migration: create English-named curated collections and fill them from static seed JSON.
# Seed file is built once by: python manage.py build_curated_collections_seed (requires OMDB_API_KEY).
# Owner: first superuser or first user.
# Seed is skipped when running under pytest or when DB name starts with test_
# (no extra data in test DB). If tests still see seeded data, run once: pytest --create-db

import json
import os
from pathlib import Path

from django.db import migrations


def load_seed_data():
    path = Path(__file__).resolve().parent.parent / 'curated_collections_seed.json'
    if not path.exists():
        return {'collections': []}
    return json.loads(path.read_text(encoding='utf-8'))


def seed_collection_movies(apps, schema_editor):
    if os.environ.get('DJANGO_TESTING') == '1':
        return
    if os.environ.get('PYTEST_CURRENT_TEST'):
        return
    db_name = schema_editor.connection.settings_dict.get('NAME', '')
    if db_name.startswith('test_'):
        return

    User = apps.get_model('auth_app', 'User')
    Collection = apps.get_model('collection', 'Collection')
    CollectionMovie = apps.get_model('collection', 'CollectionMovie')
    Movie = apps.get_model('movie', 'Movie')

    owner = User.objects.filter(is_superuser=True).first() or User.objects.first()
    if not owner:
        return

    data = load_seed_data()
    for coll_data in data.get('collections', []):
        name = coll_data.get('name', '')
        description = coll_data.get('description', '')
        design = (coll_data.get('design') or '').strip()
        coll, _ = Collection.objects.get_or_create(
            owner=owner,
            name=name,
            defaults={
                'description': description,
                'is_public': True,
                'design': design,
            },
        )
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


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('collection', '0005_seed_curated_collections'),
        ('movie', '0012_topmovie'),
    ]

    operations = [
        migrations.RunPython(seed_collection_movies, noop_reverse),
    ]
