import logging
import re
import unicodedata
from difflib import SequenceMatcher

from movie.dataclasses import AiMovie, ImdbMovie

logger = logging.getLogger(__name__)

TMDB_API_BASE_URL = 'https://api.themoviedb.org/3'
YEAR_PATTERN = re.compile(r'(\d{4})')


def normalize_title(value: str) -> str:
    text = unicodedata.normalize('NFKD', value or '')
    text = ''.join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[''`]", '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_year(value: str | None) -> str | None:
    if not value:
        return None
    match = YEAR_PATTERN.search(str(value))
    return match.group(1) if match else None


def title_similarity(left: str, right: str) -> float:
    left_norm = normalize_title(left)
    right_norm = normalize_title(right)
    if not left_norm or not right_norm:
        return 0.0
    if left_norm == right_norm:
        return 1.0
    ratio = SequenceMatcher(None, left_norm, right_norm).ratio()
    if left_norm in right_norm or right_norm in left_norm:
        ratio = max(ratio, 0.92)
    return ratio


def title_variants(title: str) -> list[str]:
    trimmed = (title or '').strip()
    if not trimmed:
        return []

    variants: list[str] = []
    seen: set[str] = set()

    def add(value: str) -> None:
        candidate = value.strip()
        if not candidate:
            return
        key = candidate.casefold()
        if key in seen:
            return
        seen.add(key)
        variants.append(candidate)

    add(trimmed)
    add(trimmed.strip('"\''))

    if ':' in trimmed:
        add(trimmed.split(':', 1)[0].strip())
    if ' - ' in trimmed:
        add(trimmed.split(' - ', 1)[0].strip())

    for candidate in list(variants):
        if candidate.lower().startswith('the '):
            add(candidate[4:].strip())
        if candidate.lower().startswith('a '):
            add(candidate[2:].strip())

    return variants


def pick_best_imdb_candidate(
    candidates: list[ImdbMovie],
    ai_title: str,
    ai_year: str | None = None,
    min_score: float = 0.55,
) -> ImdbMovie | None:
    if not candidates:
        return None

    best_item: ImdbMovie | None = None
    best_score = 0.0
    target_year = extract_year(ai_year)

    for candidate in candidates:
        score = title_similarity(ai_title, candidate.title or '')
        candidate_year = extract_year(candidate.year)
        if target_year and candidate_year:
            if candidate_year == target_year:
                score += 0.12
            else:
                score -= 0.08
        if score > best_score:
            best_score = score
            best_item = candidate

    if best_item and best_score >= min_score:
        return best_item
    return None


def build_ai_score_map(ai_movies: list[AiMovie]) -> dict[int, int]:
    return {idx: movie.match_score for idx, movie in enumerate(ai_movies)}
