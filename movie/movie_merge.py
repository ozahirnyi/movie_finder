from movie.dataclasses import OmdbMovie


def _is_blank(value: str | None) -> bool:
    if value is None:
        return True
    trimmed = value.strip()
    return not trimmed or trimmed.upper() == 'N/A'


def _merge_people(primary: list | None, fallback: list | None) -> list:
    merged = list(primary or [])
    seen = {getattr(item, 'full_name', '').casefold() for item in merged if getattr(item, 'full_name', None)}
    for item in fallback or []:
        name = getattr(item, 'full_name', '')
        if not name or name.casefold() in seen:
            continue
        merged.append(item)
        seen.add(name.casefold())
    return merged


def merge_omdb_with_tmdb_fallback(omdb_movie: OmdbMovie, tmdb_movie: OmdbMovie | None) -> OmdbMovie:
    """Keep OMDb as source of truth; fill only missing fields from TMDB."""
    if not tmdb_movie:
        return omdb_movie

    if _is_blank(omdb_movie.poster) and not _is_blank(tmdb_movie.poster):
        omdb_movie.poster = tmdb_movie.poster
    if _is_blank(omdb_movie.plot) and not _is_blank(tmdb_movie.plot):
        omdb_movie.plot = tmdb_movie.plot
    if _is_blank(omdb_movie.runtime) and not _is_blank(tmdb_movie.runtime):
        omdb_movie.runtime = tmdb_movie.runtime
    if omdb_movie.released_date is None and tmdb_movie.released_date is not None:
        omdb_movie.released_date = tmdb_movie.released_date
    if _is_blank(omdb_movie.year) and not _is_blank(tmdb_movie.year):
        omdb_movie.year = tmdb_movie.year
    if _is_blank(omdb_movie.type) and not _is_blank(tmdb_movie.type):
        omdb_movie.type = tmdb_movie.type
    if _is_blank(omdb_movie.total_seasons) and not _is_blank(tmdb_movie.total_seasons):
        omdb_movie.total_seasons = tmdb_movie.total_seasons

    if not omdb_movie.genres:
        omdb_movie.genres = tmdb_movie.genres
    if not omdb_movie.actors:
        omdb_movie.actors = tmdb_movie.actors
    if not omdb_movie.directors:
        omdb_movie.directors = tmdb_movie.directors
    if not omdb_movie.writers:
        omdb_movie.writers = tmdb_movie.writers
    if not omdb_movie.languages:
        omdb_movie.languages = tmdb_movie.languages
    if not omdb_movie.countries:
        omdb_movie.countries = tmdb_movie.countries

    omdb_movie.actors = _merge_people(omdb_movie.actors, tmdb_movie.actors)
    omdb_movie.directors = _merge_people(omdb_movie.directors, tmdb_movie.directors)
    omdb_movie.writers = _merge_people(omdb_movie.writers, tmdb_movie.writers)

    existing_sources = {rating.source for rating in (omdb_movie.ratings or [])}
    for rating in tmdb_movie.ratings or []:
        if rating.source not in existing_sources:
            omdb_movie.ratings = (omdb_movie.ratings or []) + [rating]
            existing_sources.add(rating.source)

    return omdb_movie
