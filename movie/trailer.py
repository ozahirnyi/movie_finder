import logging
import re

import requests
from django.conf import settings

logger = logging.getLogger(__name__)

TMDB_API_BASE_URL = 'https://api.themoviedb.org/3'
IMDB_ID_PATTERN = re.compile(r'^tt\d+$', re.IGNORECASE)


def build_trailer_search_query(title: str, year: str | None = None) -> str | None:
    trimmed_title = (title or '').strip()
    if not trimmed_title:
        return None
    trimmed_year = (year or '').strip()
    return f'{trimmed_title} {trimmed_year} trailer' if trimmed_year else f'{trimmed_title} trailer'


def _normalize_imdb_id(imdb_id: str | None) -> str | None:
    trimmed = (imdb_id or '').strip()
    if not trimmed or not IMDB_ID_PATTERN.match(trimmed):
        return None
    return trimmed.lower()


def _pick_youtube_video_key(videos: list[dict]) -> str | None:
    youtube_videos = [video for video in videos if (video.get('site') or '').lower() == 'youtube']
    if not youtube_videos:
        return None

    def sort_key(video: dict) -> tuple[int, int, int]:
        video_type = (video.get('type') or '').lower()
        is_trailer = video_type == 'trailer'
        is_official = bool(video.get('official'))
        return (1 if is_trailer else 0, 1 if is_official else 0, 0)

    youtube_videos.sort(key=sort_key, reverse=True)
    for video in youtube_videos:
        key = video.get('key')
        if isinstance(key, str) and key.strip():
            return key.strip()
    return None


def _fetch_tmdb_videos(media_type: str, tmdb_id: int, api_key: str) -> list[dict]:
    try:
        response = requests.get(
            f'{TMDB_API_BASE_URL}/{media_type}/{tmdb_id}/videos',
            params={'api_key': api_key},
            timeout=10,
        )
    except requests.RequestException:
        logger.exception('TMDB videos lookup request failed for %s/%s', media_type, tmdb_id)
        return []

    if not response.ok:
        logger.warning(
            'TMDB videos lookup failed for %s/%s with status %s',
            media_type,
            tmdb_id,
            response.status_code,
        )
        return []

    payload = response.json()
    results = payload.get('results')
    return results if isinstance(results, list) else []


def lookup_tmdb_trailer_video_id(imdb_id: str | None) -> str | None:
    normalized_imdb_id = _normalize_imdb_id(imdb_id)
    if not normalized_imdb_id:
        return None

    api_key = getattr(settings, 'TMDB_API_KEY', '') or ''
    if not api_key.strip():
        logger.warning('TMDB_API_KEY is not configured; TMDB trailer lookup skipped')
        return None

    try:
        response = requests.get(
            f'{TMDB_API_BASE_URL}/find/{normalized_imdb_id}',
            params={'external_source': 'imdb_id', 'api_key': api_key},
            timeout=10,
        )
    except requests.RequestException:
        logger.exception('TMDB find lookup request failed for %s', normalized_imdb_id)
        return None

    if not response.ok:
        logger.warning(
            'TMDB find lookup failed for %s with status %s',
            normalized_imdb_id,
            response.status_code,
        )
        return None

    payload = response.json()
    candidates: list[tuple[str, int]] = []
    for media_type in ('movie', 'tv'):
        results = payload.get(f'{media_type}_results')
        if not isinstance(results, list):
            continue
        for item in results:
            if not isinstance(item, dict):
                continue
            tmdb_id = item.get('id')
            if isinstance(tmdb_id, int):
                candidates.append((media_type, tmdb_id))

    for media_type, tmdb_id in candidates:
        videos = _fetch_tmdb_videos(media_type, tmdb_id, api_key)
        video_key = _pick_youtube_video_key(videos)
        if video_key:
            return video_key

    return None


def lookup_youtube_trailer_video_id(title: str, year: str | None = None) -> str | None:
    query = build_trailer_search_query(title, year)
    if not query:
        return None

    api_key = getattr(settings, 'YOUTUBE_API_KEY', '') or ''
    if not api_key.strip():
        logger.warning('YOUTUBE_API_KEY is not configured; YouTube trailer lookup skipped')
        return None

    try:
        response = requests.get(
            'https://www.googleapis.com/youtube/v3/search',
            params={
                'part': 'snippet',
                'type': 'video',
                'maxResults': 1,
                'videoEmbeddable': 'true',
                'q': query,
                'key': api_key,
            },
            timeout=10,
        )
    except requests.RequestException:
        logger.exception('YouTube trailer lookup request failed')
        return None

    if not response.ok:
        logger.warning('YouTube trailer lookup failed with status %s', response.status_code)
        return None

    payload = response.json()
    items = payload.get('items') or []
    if not items:
        return None

    video_id = items[0].get('id', {}).get('videoId')
    return video_id if isinstance(video_id, str) and video_id else None


def lookup_trailer_video_id(title: str, year: str | None = None, imdb_id: str | None = None) -> str | None:
    video_id = lookup_tmdb_trailer_video_id(imdb_id)
    if video_id:
        return video_id
    return lookup_youtube_trailer_video_id(title, year)
