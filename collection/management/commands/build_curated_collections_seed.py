"""
Fetch OMDb once per title from curated_collections_data and write
collection/curated_collections_seed.json. Run once, commit the JSON; migration 0006 reads it.
"""
import json
import time
from pathlib import Path

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from collection.curated_collections_data import COLLECTIONS


def _fetch_omdb_movie(title: str, api_url: str, api_key: str) -> dict | None:
    from urllib.parse import quote_plus

    url = f'{api_url}/?apikey={api_key}&t={quote_plus(title)}'
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        if data.get('Response') != 'True' or data.get('Error') or not data.get('imdbID'):
            return None
        return data
    except Exception:
        return None
    finally:
        time.sleep(0.25)


class Command(BaseCommand):
    help = 'Fetch OMDb for curated collection titles and write curated_collections_seed.json'

    def handle(self, *args, **options):
        api_url = getattr(settings, 'OMDB_API_URL', 'http://www.omdbapi.com')
        api_key = getattr(settings, 'OMDB_API_KEY', '') or ''
        if not api_key or api_key == 'omdb_api_key':
            self.stderr.write(self.style.ERROR('Set OMDB_API_KEY in .env'))
            return

        out_path = Path(__file__).resolve().parent.parent.parent / 'curated_collections_seed.json'
        result = {'collections': []}

        for name, description, design, titles in COLLECTIONS:
            movies = []
            for position, title in enumerate(titles, start=0):
                data = _fetch_omdb_movie(title, api_url, api_key)
                if not data:
                    self.stdout.write(self.style.WARNING(f'Skip (not found): {title!r}'))
                    continue
                imdb_id = (data.get('imdbID') or '').strip()
                if not imdb_id:
                    continue
                movies.append({
                    'position': position,
                    'imdb_id': imdb_id,
                    'title': data.get('Title') or title,
                    'year': data.get('Year') or '',
                    'type': data.get('Type') or 'movie',
                    'poster': data.get('Poster') or '',
                    'plot': data.get('Plot') or '',
                })
            result['collections'].append({
                'name': name,
                'description': description,
                'design': design,
                'movies': movies,
            })
            self.stdout.write(f'{name}: {len(movies)} movies')

        out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
        self.stdout.write(self.style.SUCCESS(f'Wrote {out_path}'))
