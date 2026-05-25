import logging
from dataclasses import dataclass
from datetime import datetime

import requests
from django.conf import settings

from movie.dataclasses import (
    Actor,
    Country,
    Director,
    Genre,
    Language,
    OmdbMovie,
    Rating,
    Writer,
)

from .ai_resolve import TMDB_API_BASE_URL, extract_year, title_similarity

logger = logging.getLogger(__name__)

TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'
TMDB_MIN_MATCH_SCORE = 0.55


@dataclass
class TmdbMatch:
    media_type: str
    tmdb_id: int
    title: str
    year: str | None
    imdb_id: str | None
    score: float


def get_tmdb_api_key() -> str | None:
    api_key = getattr(settings, 'TMDB_API_KEY', '') or ''
    return api_key.strip() or None


def _build_poster_url(poster_path: str | None) -> str | None:
    if not poster_path:
        return None
    return f'{TMDB_IMAGE_BASE_URL}{poster_path}'


def search_tmdb_match(title: str, year: str | None = None, min_score: float = TMDB_MIN_MATCH_SCORE) -> TmdbMatch | None:
    api_key = get_tmdb_api_key()
    if not api_key:
        return None

    target_year = extract_year(year)
    search_configs = (
        ('movie', 'primary_release_year'),
        ('tv', 'first_air_date_year'),
    )

    best_match: TmdbMatch | None = None

    for media_type, year_param in search_configs:
        params = {'api_key': api_key, 'query': title}
        if target_year:
            params[year_param] = target_year
        try:
            response = requests.get(
                f'{TMDB_API_BASE_URL}/search/{media_type}',
                params=params,
                timeout=10,
            )
        except requests.RequestException:
            logger.exception('TMDB search failed for title=%r', title)
            continue

        if not response.ok:
            logger.warning('TMDB search failed for title=%r status=%s', title, response.status_code)
            continue

        results = response.json().get('results') or []
        if not isinstance(results, list):
            continue

        for item in results[:8]:
            if not isinstance(item, dict):
                continue
            candidate_title = item.get('title') or item.get('name') or ''
            score = title_similarity(title, candidate_title)
            release_date = item.get('release_date') or item.get('first_air_date') or ''
            candidate_year = extract_year(release_date)
            if target_year and candidate_year:
                if candidate_year == target_year:
                    score += 0.12
                else:
                    score -= 0.08
            if score < min_score:
                continue
            if best_match and score <= best_match.score:
                continue

            tmdb_id = item.get('id')
            if not isinstance(tmdb_id, int):
                continue

            best_match = TmdbMatch(
                media_type=media_type,
                tmdb_id=tmdb_id,
                title=candidate_title,
                year=candidate_year,
                imdb_id=None,
                score=score,
            )

    if not best_match:
        return None

    imdb_id = fetch_tmdb_imdb_id(best_match.media_type, best_match.tmdb_id, api_key)
    if imdb_id:
        best_match.imdb_id = imdb_id
    return best_match


def fetch_tmdb_imdb_id(media_type: str, tmdb_id: int, api_key: str | None = None) -> str | None:
    resolved_key = api_key or get_tmdb_api_key()
    if not resolved_key:
        return None

    try:
        response = requests.get(
            f'{TMDB_API_BASE_URL}/{media_type}/{tmdb_id}/external_ids',
            params={'api_key': resolved_key},
            timeout=10,
        )
    except requests.RequestException:
        logger.exception('TMDB external_ids lookup failed for %s/%s', media_type, tmdb_id)
        return None

    if not response.ok:
        return None

    imdb_id = response.json().get('imdb_id')
    if isinstance(imdb_id, str) and imdb_id.startswith('tt'):
        return imdb_id
    return None


def lookup_imdb_id_via_tmdb(title: str, year: str | None = None) -> str | None:
    match = search_tmdb_match(title, year)
    return match.imdb_id if match else None


def get_movie_from_tmdb(media_type: str, tmdb_id: int) -> OmdbMovie | None:
    api_key = get_tmdb_api_key()
    if not api_key:
        return None

    try:
        response = requests.get(
            f'{TMDB_API_BASE_URL}/{media_type}/{tmdb_id}',
            params={
                'api_key': api_key,
                'append_to_response': 'external_ids,credits',
            },
            timeout=15,
        )
    except requests.RequestException:
        logger.exception('TMDB details lookup failed for %s/%s', media_type, tmdb_id)
        return None

    if not response.ok:
        logger.warning('TMDB details lookup failed for %s/%s status=%s', media_type, tmdb_id, response.status_code)
        return None

    payload = response.json()
    if not isinstance(payload, dict):
        return None

    return _map_tmdb_payload_to_omdb_movie(payload, media_type)


def _parse_release_date(value: str | None):
    if not value:
        return None
    try:
        return datetime.strptime(value, '%Y-%m-%d').date()
    except ValueError:
        return None


def _map_tmdb_payload_to_omdb_movie(payload: dict, media_type: str) -> OmdbMovie | None:
    title = payload.get('title') or payload.get('name')
    if not title:
        return None

    release_date = payload.get('release_date') or payload.get('first_air_date')
    year = extract_year(release_date)

    runtime_value = payload.get('runtime')
    if runtime_value is None:
        episode_runtimes = payload.get('episode_run_time') or []
        if isinstance(episode_runtimes, list) and episode_runtimes:
            runtime_value = episode_runtimes[0]
    runtime = f'{runtime_value} min' if runtime_value else None

    genres = payload.get('genres') or []
    genre_dtos = [
        Genre(name=item.get('name').strip())
        for item in genres
        if isinstance(item, dict) and isinstance(item.get('name'), str) and item.get('name').strip()
    ]

    credits = payload.get('credits') if isinstance(payload.get('credits'), dict) else {}
    crew = credits.get('crew') if isinstance(credits.get('crew'), list) else []
    cast = credits.get('cast') if isinstance(credits.get('cast'), list) else []

    directors = [
        Director(full_name=member.get('name').strip())
        for member in crew
        if isinstance(member, dict)
        and member.get('job') == 'Director'
        and isinstance(member.get('name'), str)
        and member.get('name').strip()
    ]
    writers = [
        Writer(full_name=member.get('name').strip())
        for member in crew
        if isinstance(member, dict)
        and member.get('job') in {'Writer', 'Screenplay', 'Story'}
        and isinstance(member.get('name'), str)
        and member.get('name').strip()
    ]
    actors = [
        Actor(full_name=member.get('name').strip())
        for member in cast[:8]
        if isinstance(member, dict) and isinstance(member.get('name'), str) and member.get('name').strip()
    ]

    languages = [
        Language(name=item.get('english_name') or item.get('name') or '')
        for item in (payload.get('spoken_languages') or [])
        if isinstance(item, dict) and (item.get('english_name') or item.get('name'))
    ]
    countries = [
        Country(name=item.get('name').strip())
        for item in (payload.get('production_countries') or [])
        if isinstance(item, dict) and isinstance(item.get('name'), str) and item.get('name').strip()
    ]

    external_ids = payload.get('external_ids') if isinstance(payload.get('external_ids'), dict) else {}
    imdb_id = external_ids.get('imdb_id')
    if not (isinstance(imdb_id, str) and imdb_id.startswith('tt')):
        imdb_id = None

    vote_average = payload.get('vote_average')
    ratings = []
    if vote_average is not None:
        ratings.append(Rating(source='TMDB', value=f'{vote_average}/10'))

    return OmdbMovie(
        title=title,
        year=year,
        released_date=_parse_release_date(release_date),
        runtime=runtime,
        genres=genre_dtos,
        directors=directors,
        writers=writers,
        actors=actors,
        plot=payload.get('overview') or None,
        languages=languages,
        countries=countries,
        awards=None,
        poster=_build_poster_url(payload.get('poster_path')),
        ratings=ratings,
        metascore=None,
        imdb_rating=None,
        imdb_votes=None,
        imdb_id=imdb_id,
        type='series' if media_type == 'tv' else 'movie',
        total_seasons=str(payload.get('number_of_seasons')) if payload.get('number_of_seasons') else None,
    )


def get_movie_from_tmdb_by_title(title: str, year: str | None = None) -> OmdbMovie | None:
    match = search_tmdb_match(title, year)
    if not match:
        return None
    return get_movie_from_tmdb(match.media_type, match.tmdb_id)
