import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from urllib.parse import quote_plus

import requests
from django.conf import settings
from django.contrib.postgres.aggregates import ArrayAgg, JSONBAgg
from django.db import close_old_connections, transaction
from django.db.models import Case, Count, F, IntegerField, JSONField, Q, Value, When
from django.db.models.functions import JSONObject
from django.utils import timezone

from movie.dataclasses import (
    Actor as ActorDTO,
)
from movie.dataclasses import (
    AiMovie,
    ImdbMovie,
    MovieRecommendation,
    OmdbMovie,
    UserActivitySummary,
)
from movie.dataclasses import (
    Country as CountryDTO,
)
from movie.dataclasses import (
    Director as DirectorDTO,
)
from movie.dataclasses import (
    Genre as GenreDTO,
)
from movie.dataclasses import (
    Language as LanguageDTO,
)
from movie.dataclasses import (
    Rating as RatingDTO,
)
from movie.dataclasses import (
    Writer as WriterDTO,
)
from movie.models import Actor, Country, Director, Genre, Language, LikeMovie, Movie, Rating, RecommendedMovie, TopMovie, WatchLaterMovie, Writer

from .ai_resolve import (
    pick_best_imdb_candidate,
    title_variants,
)
from .movie_merge import _is_blank, merge_omdb_with_tmdb_fallback
from .tmdb_client import get_movie_from_tmdb, search_tmdb_match

logger = logging.getLogger(__name__)


class MovieRepository:
    def get_movies_from_imdb(self, expression: str) -> list[ImdbMovie]:
        response = requests.get(
            settings.IMDB_API_SEARCH_BY_NAME_URL + '?query=' + expression,
            headers={
                'authorization': settings.IMDB_API_KEY,
                'content-type': 'application/json',
            },
            timeout=30,
        )
        logger.info(
            'IMDB/CollectAPI response: status=%s expression=%r body_prefix=%r',
            response.status_code,
            expression,
            (response.text[:500] if response.text else ''),
        )
        response.raise_for_status()

        try:
            response_data = json.loads(response.text)
        except json.JSONDecodeError as e:
            raise Exception(f'Invalid JSON response from IMDB API: {e}') from e

        if 'result' not in response_data:
            return []

        if not isinstance(response_data['result'], list):
            return []

        imdb_movies = []
        for data in response_data['result']:
            if not isinstance(data, dict):
                continue
            try:
                imdb_movies.append(
                    ImdbMovie(
                        title=data.get('Title', ''),
                        imdb_id=data.get('imdbID', ''),
                        poster=data.get('Poster', ''),
                        year=data.get('Year', ''),
                        type=data.get('Type', ''),
                    )
                )
            except (KeyError, TypeError):
                continue

        return imdb_movies

    def get_movies_from_omdb_search(self, expression: str) -> list[ImdbMovie]:
        """Search movies via OMDb API (?s=). Returns list of ImdbMovie."""
        url = f'{settings.OMDB_API_URL}/?apikey={settings.OMDB_API_KEY}&s={quote_plus(expression)}'
        response = requests.get(url, headers={'content-type': 'application/json'}, timeout=30)
        logger.info(
            'OMDb search response: status=%s expression=%r body_prefix=%r',
            response.status_code,
            expression,
            (response.text[:500] if response.text else ''),
        )
        response.raise_for_status()
        data = response.json()
        if data.get('Response') == 'False' or data.get('Error'):
            logger.info('OMDb search returned no results: expression=%r error=%r', expression, data.get('Error'))
            return []
        search_list = data.get('Search') or []
        if not isinstance(search_list, list):
            return []
        result = []
        for item in search_list:
            if not isinstance(item, dict):
                continue
            try:
                result.append(
                    ImdbMovie(
                        title=item.get('Title', ''),
                        imdb_id=item.get('imdbID', ''),
                        poster=item.get('Poster', ''),
                        year=item.get('Year', ''),
                        type=item.get('Type', 'movie'),
                    )
                )
            except (KeyError, TypeError):
                continue
        return result

    def get_movies_from_db_search(self, expression: str, limit: int = 20) -> list[ImdbMovie]:
        """Fallback: search movies in our DB by title (icontains)."""
        qs = Movie.objects.filter(title__icontains=expression).order_by('title')[:limit]
        return [
            ImdbMovie(
                title=m.title,
                imdb_id=m.imdb_id,
                poster=m.poster or '',
                year=m.year or '',
                type=m.type or 'movie',
            )
            for m in qs
        ]

    @staticmethod
    def get_movie_from_omdb_by_expression(title: str, year: str | None = None) -> OmdbMovie | None:
        def _replace_not_available(value):
            if isinstance(value, dict):
                return {key: _replace_not_available(val) for key, val in value.items()}
            if isinstance(value, list):
                return [_replace_not_available(item) for item in value]
            if isinstance(value, str) and value.strip().upper() == 'N/A':
                return None
            return value

        try:
            params = f't={quote_plus(title)}&apikey={settings.OMDB_API_KEY}'
            release_year = (year or '').strip()
            if release_year.isdigit():
                params += f'&y={release_year[:4]}'
            response = requests.get(
                f'{settings.OMDB_API_URL}?{params}',
                headers={'content-type': 'application/json'},
                timeout=30,
            )
            logger.info(
                'OMDB response: status=%s title=%r body_prefix=%r',
                response.status_code,
                title,
                (response.text[:500] if response.text else ''),
            )
            data = _replace_not_available(response.json())
            if data.get('Response') == 'False' or data.get('Error'):
                logger.info('OMDB movie not found: title=%r error=%r', title, data.get('Error'))
                return None
            omdb_movie = OmdbMovie(
                title=data.get('Title'),
                year=data.get('Year'),
                released_date=datetime.strptime(data['Released'], '%d %b %Y').date() if data.get('Released') else None,
                runtime=data.get('Runtime'),
                genres=[Genre(name=name.strip()) for name in (data.get('Genre') or '').split(',') if name.strip()],
                directors=[Director(full_name=name.strip()) for name in (data.get('Director') or '').split(',') if name.strip()],
                writers=[Writer(full_name=name.strip()) for name in (data.get('Writer') or '').split(',') if name.strip()],
                actors=[Actor(full_name=name.strip()) for name in (data.get('Actors') or '').split(',') if name.strip()],
                plot=data.get('Plot'),
                languages=[Language(name=name.strip()) for name in (data.get('Language') or '').split(',') if name.strip()],
                countries=[Country(name=name.strip()) for name in (data.get('Country') or '').split(',') if name.strip()],
                awards=data.get('Awards'),
                poster=data.get('Poster'),
                ratings=[Rating(source=rating.get('Source'), value=rating.get('Value')) for rating in (data.get('Ratings') or []) if rating],
                metascore=data.get('Metascore'),
                imdb_rating=data.get('imdbRating'),
                imdb_votes=data.get('imdbVotes'),
                imdb_id=data.get('imdbID'),
                type=data.get('Type'),
                total_seasons=data.get('totalSeasons'),
            )
            return omdb_movie
        except Exception as e:
            logger.exception('OMDB request failed: title=%r error=%s', title, e)
            raise Exception(f'Error while getting movies from OMDB: {e}')

    def get_movie_from_omdb_by_id(self, imdb_id: str) -> OmdbMovie | None:
        """Fetch full movie details by IMDb ID (OMDb ?i=). Use when we have id from search to avoid duplicate rows."""

        def _replace_not_available(value):
            if isinstance(value, dict):
                return {key: _replace_not_available(val) for key, val in value.items()}
            if isinstance(value, list):
                return [_replace_not_available(item) for item in value]
            if isinstance(value, str) and value.strip().upper() == 'N/A':
                return None
            return value

        if not (imdb_id and imdb_id.strip()):
            return None
        try:
            response = requests.get(
                f'{settings.OMDB_API_URL}?i={quote_plus(imdb_id.strip())}&apikey={settings.OMDB_API_KEY}',
                headers={'content-type': 'application/json'},
                timeout=30,
            )
            response.raise_for_status()
            data = _replace_not_available(response.json())
            if data.get('Response') == 'False' or data.get('Error'):
                return None
            return OmdbMovie(
                title=data.get('Title'),
                year=data.get('Year'),
                released_date=datetime.strptime(data['Released'], '%d %b %Y').date() if data.get('Released') else None,
                runtime=data.get('Runtime'),
                genres=[Genre(name=name.strip()) for name in (data.get('Genre') or '').split(',') if name.strip()],
                directors=[Director(full_name=name.strip()) for name in (data.get('Director') or '').split(',') if name.strip()],
                writers=[Writer(full_name=name.strip()) for name in (data.get('Writer') or '').split(',') if name.strip()],
                actors=[Actor(full_name=name.strip()) for name in (data.get('Actors') or '').split(',') if name.strip()],
                plot=data.get('Plot'),
                languages=[Language(name=name.strip()) for name in (data.get('Language') or '').split(',') if name.strip()],
                countries=[Country(name=name.strip()) for name in (data.get('Country') or '').split(',') if name.strip()],
                awards=data.get('Awards'),
                poster=data.get('Poster'),
                ratings=[Rating(source=r.get('Source'), value=r.get('Value')) for r in (data.get('Ratings') or []) if r],
                metascore=data.get('Metascore'),
                imdb_rating=data.get('imdbRating'),
                imdb_votes=data.get('imdbVotes'),
                imdb_id=data.get('imdbID'),
                type=data.get('Type'),
                total_seasons=data.get('totalSeasons'),
            )
        except Exception as e:
            logger.warning('OMDB request by id failed: imdb_id=%r error=%s', imdb_id, e)
            return None

    def _create_movie_in_db(self, omdb_movie: OmdbMovie) -> Movie:
        def _normalize_char(value: str | None) -> str:
            return value or ''

        with transaction.atomic():
            movie_instance, created = Movie.objects.get_or_create(
                imdb_id=omdb_movie.imdb_id,
                defaults={
                    'title': _normalize_char(omdb_movie.title),
                    'year': _normalize_char(omdb_movie.year),
                    'released_date': omdb_movie.released_date,
                    'runtime': _normalize_char(omdb_movie.runtime),
                    'plot': _normalize_char(omdb_movie.plot),
                    'awards': _normalize_char(omdb_movie.awards),
                    'poster': _normalize_char(omdb_movie.poster),
                    'metascore': _normalize_char(omdb_movie.metascore),
                    'imdb_rating': _normalize_char(omdb_movie.imdb_rating),
                    'imdb_votes': _normalize_char(omdb_movie.imdb_votes),
                    'type': _normalize_char(omdb_movie.type),
                    'total_seasons': _normalize_char(omdb_movie.total_seasons),
                },
            )
            if created:
                if omdb_movie.genres:
                    genres = [Genre.objects.get_or_create(name=g.name)[0] for g in omdb_movie.genres]
                    movie_instance.genres.set(genres)
                if omdb_movie.actors:
                    actors = [Actor.objects.get_or_create(full_name=a.full_name)[0] for a in omdb_movie.actors]
                    movie_instance.actors.set(actors)
                if omdb_movie.directors:
                    directors_list = [Director.objects.get_or_create(full_name=d.full_name)[0] for d in omdb_movie.directors]
                    movie_instance.directors.set(directors_list)
                if omdb_movie.ratings:
                    ratings = [Rating(source=r.source, value=r.value, movie_id=movie_instance.id) for r in omdb_movie.ratings]
                    Rating.objects.bulk_create(ratings)
                if omdb_movie.languages:
                    languages = [Language.objects.get_or_create(name=lang.name)[0] for lang in omdb_movie.languages]
                    movie_instance.languages.set(languages)
                if omdb_movie.countries:
                    countries = [Country.objects.get_or_create(name=c.name)[0] for c in omdb_movie.countries]
                    movie_instance.countries.set(countries)
                if omdb_movie.writers:
                    writers = [Writer.objects.get_or_create(full_name=w.full_name)[0] for w in omdb_movie.writers]
                    movie_instance.writers.set(writers)
            return movie_instance

    def search_movies_in_omdb_from_imdb_list(self, imdb_movies: list[ImdbMovie], initiator_id: int) -> list[OmdbMovie]:
        """Resolve ImdbMovie list (from OMDb search) to OmdbMovie with DB lookup by imdb_id first. Avoids duplicates."""
        if not imdb_movies:
            return []

        def _resolve_imdb_item(imdb_item: ImdbMovie) -> OmdbMovie | None:
            try:
                if imdb_item.imdb_id and imdb_item.imdb_id.strip():
                    movie_instance = (
                        Movie.objects.filter(imdb_id=imdb_item.imdb_id.strip())
                        .with_is_liked(initiator_id)
                        .with_is_watch_later(initiator_id)
                        .with_is_watched(initiator_id)
                        .with_likes_count()
                        .with_watch_later_count()
                        .first()
                    )
                    if movie_instance:
                        return self._movie_to_omdb_dto(movie_instance)
                    omdb_movie = self.get_movie_from_omdb_by_id(imdb_item.imdb_id.strip())
                    if omdb_movie and omdb_movie.imdb_id:
                        saved_movie = self._create_movie_in_db(omdb_movie)
                        omdb_movie.id = saved_movie.id
                        return omdb_movie
                    return None
                return self._resolve_one_by_title(imdb_item.title, initiator_id)
            except Exception as exc:
                logger.warning('Parallel imdb-list resolve failed: title=%r error=%s', imdb_item.title, exc)
                return None
            finally:
                close_old_connections()

        max_workers = min(len(imdb_movies), 5)
        results_by_index: dict[int, OmdbMovie] = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_idx = {executor.submit(_resolve_imdb_item, item): i for i, item in enumerate(imdb_movies)}
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                result = future.result()
                if result:
                    results_by_index[idx] = result

        return [results_by_index[i] for i in sorted(results_by_index)]

    def _movie_to_omdb_dto(self, movie_instance: Movie) -> OmdbMovie:
        return OmdbMovie(
            id=movie_instance.id,
            title=movie_instance.title,
            year=movie_instance.year,
            released_date=movie_instance.released_date,
            runtime=movie_instance.runtime,
            genres=[GenreDTO(g.name) for g in movie_instance.genres.all()],
            directors=[DirectorDTO(d.full_name) for d in movie_instance.directors.all()],
            writers=[WriterDTO(w.full_name) for w in movie_instance.writers.all()],
            actors=[ActorDTO(a.full_name) for a in movie_instance.actors.all()],
            plot=movie_instance.plot,
            languages=[LanguageDTO(lang.name) for lang in movie_instance.languages.all()],
            countries=[CountryDTO(c.name) for c in movie_instance.countries.all()],
            awards=movie_instance.awards,
            poster=movie_instance.poster,
            ratings=[RatingDTO(r.source, r.value) for r in movie_instance.movie_ratings.all()],
            metascore=movie_instance.metascore,
            imdb_rating=movie_instance.imdb_rating,
            imdb_votes=movie_instance.imdb_votes,
            imdb_id=movie_instance.imdb_id,
            type=movie_instance.type,
            total_seasons=movie_instance.total_seasons,
            likes_count=getattr(movie_instance, 'likes_count', 0),
            is_liked=getattr(movie_instance, 'is_liked', False),
            watch_later_count=getattr(movie_instance, 'watch_later_count', 0),
            is_watch_later=getattr(movie_instance, 'is_watch_later', False),
            is_watched=getattr(movie_instance, 'is_watched', False),
        )

    def _resolve_one_by_title(self, title: str, initiator_id: int, year: str | None = None) -> OmdbMovie | None:
        movie_instance = (
            Movie.objects.filter(title__iexact=title)
            .with_is_liked(initiator_id)
            .with_is_watch_later(initiator_id)
            .with_is_watched(initiator_id)
            .with_likes_count()
            .with_watch_later_count()
            .first()
        )
        if movie_instance:
            return self._movie_to_omdb_dto(movie_instance)

        for candidate_title in title_variants(title):
            omdb_movie = self.get_movie_from_omdb_by_expression(candidate_title, year)
            if omdb_movie is None:
                imdb_list = self.get_movies_from_omdb_search(candidate_title)
                best_match = pick_best_imdb_candidate(imdb_list, title, year)
                if best_match and best_match.imdb_id:
                    omdb_movie = self.get_movie_from_omdb_by_id(best_match.imdb_id)
            if omdb_movie is None:
                continue
            if omdb_movie.imdb_id:
                saved_movie = self._create_movie_in_db(omdb_movie)
                omdb_movie.id = saved_movie.id
                return omdb_movie
            omdb_movie.id = 0
            return omdb_movie

        return None

    def _movie_from_db_by_imdb_id(self, imdb_id: str, initiator_id: int) -> OmdbMovie | None:
        movie_instance = (
            Movie.objects.filter(imdb_id=imdb_id)
            .with_is_liked(initiator_id)
            .with_is_watch_later(initiator_id)
            .with_is_watched(initiator_id)
            .with_likes_count()
            .with_watch_later_count()
            .first()
        )
        if movie_instance:
            return self._movie_to_omdb_dto(movie_instance)
        return None

    def _persist_resolved_movie(self, omdb_movie: OmdbMovie, initiator_id: int) -> OmdbMovie | None:
        if not omdb_movie.imdb_id:
            return None
        saved_movie = self._create_movie_in_db(omdb_movie)
        persisted = self._movie_from_db_by_imdb_id(saved_movie.imdb_id, initiator_id)
        return persisted or omdb_movie

    def _resolve_via_tmdb(self, ai_movie: AiMovie, initiator_id: int) -> OmdbMovie | None:
        title = (ai_movie.title or '').strip()
        if not title:
            return None

        match = search_tmdb_match(title, ai_movie.year)
        if not match:
            return None

        imdb_id = match.imdb_id
        if imdb_id:
            existing = self._movie_from_db_by_imdb_id(imdb_id, initiator_id)
            if existing:
                return existing

            omdb_movie = self.get_movie_from_omdb_by_id(imdb_id)
            if omdb_movie:
                tmdb_movie = None
                if _is_blank(omdb_movie.poster):
                    tmdb_movie = get_movie_from_tmdb(match.media_type, match.tmdb_id)
                return self._persist_resolved_movie(
                    merge_omdb_with_tmdb_fallback(omdb_movie, tmdb_movie),
                    initiator_id,
                )

        tmdb_movie = get_movie_from_tmdb(match.media_type, match.tmdb_id)
        if not tmdb_movie:
            return None

        imdb_id = tmdb_movie.imdb_id or imdb_id
        if imdb_id:
            existing = self._movie_from_db_by_imdb_id(imdb_id, initiator_id)
            if existing:
                return existing

            omdb_movie = self.get_movie_from_omdb_by_id(imdb_id)
            if omdb_movie:
                return self._persist_resolved_movie(
                    merge_omdb_with_tmdb_fallback(omdb_movie, tmdb_movie),
                    initiator_id,
                )

        omdb_by_title = self.get_movie_from_omdb_by_expression(
            tmdb_movie.title,
            tmdb_movie.year or ai_movie.year,
        )
        if omdb_by_title and omdb_by_title.imdb_id:
            return self._persist_resolved_movie(
                merge_omdb_with_tmdb_fallback(omdb_by_title, tmdb_movie),
                initiator_id,
            )

        return None

    def _resolve_ai_movie(self, ai_movie: AiMovie, initiator_id: int) -> OmdbMovie | None:
        title = (ai_movie.title or '').strip()
        if not title:
            return None

        existing = (
            Movie.objects.filter(title__iexact=title)
            .with_is_liked(initiator_id)
            .with_is_watch_later(initiator_id)
            .with_is_watched(initiator_id)
            .with_likes_count()
            .with_watch_later_count()
            .first()
        )
        if existing:
            return self._movie_to_omdb_dto(existing)

        tmdb_resolved = self._resolve_via_tmdb(ai_movie, initiator_id)
        if tmdb_resolved:
            return tmdb_resolved

        resolved = self._resolve_one_by_title(title, initiator_id, ai_movie.year)
        if resolved:
            return resolved

        for variant in title_variants(title)[1:]:
            imdb_list = self.get_movies_from_omdb_search(variant)
            best_match = pick_best_imdb_candidate(imdb_list, title, ai_movie.year)
            if best_match and best_match.imdb_id:
                omdb_movie = self.get_movie_from_omdb_by_id(best_match.imdb_id)
                if omdb_movie and omdb_movie.imdb_id:
                    saved_movie = self._create_movie_in_db(omdb_movie)
                    omdb_movie.id = saved_movie.id
                    return omdb_movie

        db_matches = self.get_movies_from_db_search(title, limit=5)
        best_match = pick_best_imdb_candidate(db_matches, title, ai_movie.year)
        if best_match:
            if best_match.imdb_id:
                return self._resolve_one_by_title(best_match.title, initiator_id, best_match.year or ai_movie.year)
            return self._resolve_one_by_title(best_match.title, initiator_id, ai_movie.year)

        return None

    def resolve_ai_movie(self, ai_movie: AiMovie, initiator_id: int) -> OmdbMovie | None:
        movie = self._resolve_ai_movie(ai_movie, initiator_id)
        if movie:
            movie.match_score = ai_movie.match_score
        return movie

    def resolve_ai_movies(self, ai_movies: list[AiMovie], initiator_id: int) -> list[OmdbMovie]:
        if not ai_movies:
            return []

        resolved_by_index: dict[int, OmdbMovie] = {}

        def _resolve_safe(index: int, ai_movie: AiMovie) -> tuple[int, OmdbMovie | None]:
            try:
                return index, self._resolve_ai_movie(ai_movie, initiator_id)
            except Exception as exc:
                logger.warning('AI movie resolve failed: title=%r error=%s', ai_movie.title, exc)
                return index, None
            finally:
                close_old_connections()

        max_workers = min(len(ai_movies), 8)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(_resolve_safe, index, ai_movie) for index, ai_movie in enumerate(ai_movies)]
            for future in as_completed(futures):
                index, movie = future.result()
                if movie:
                    movie.match_score = ai_movies[index].match_score
                    resolved_by_index[index] = movie

        return [resolved_by_index[index] for index in sorted(resolved_by_index)]

    def resolve_ai_movies_as_completed(self, ai_movies: list[AiMovie], initiator_id: int):
        if not ai_movies:
            return

        def _resolve_safe(index: int, ai_movie: AiMovie) -> tuple[int, OmdbMovie | None]:
            try:
                return index, self._resolve_ai_movie(ai_movie, initiator_id)
            except Exception as exc:
                logger.warning('AI movie resolve failed: title=%r error=%s', ai_movie.title, exc)
                return index, None
            finally:
                close_old_connections()

        max_workers = min(len(ai_movies), 8)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_index = {
                executor.submit(_resolve_safe, index, ai_movie): index for index, ai_movie in enumerate(ai_movies)
            }
            for future in as_completed(future_to_index):
                index, movie = future.result()
                if movie:
                    movie.match_score = ai_movies[index].match_score
                yield index, movie

    def search_movies_in_omdb(self, movie_titles: list[str], initiator_id: int) -> list[OmdbMovie]:
        ai_movies = [AiMovie(title=title) for title in movie_titles if title]
        return self.resolve_ai_movies(ai_movies, initiator_id)


class RecommendationRepository:
    def get_cached_movie_ids(self, user_id: int, recommendation_date) -> list[int]:
        return list(
            RecommendedMovie.objects.filter(
                user_id=user_id,
                recommendation_date=recommendation_date,
                is_active=True,
            ).values_list('movie_id', flat=True)
        )

    def get_movies_by_ids(self, movie_ids: list[int], user_id: int) -> list[MovieRecommendation]:
        if not movie_ids:
            return []
        queryset = self._recommendation_queryset(user_id).filter(id__in=set(movie_ids))
        return [self._to_recommendation_dto(movie) for movie in queryset]

    def get_movies_by_titles(self, titles: list[str], user_id: int) -> list[MovieRecommendation]:
        if not titles:
            return []
        queryset = (
            self._recommendation_queryset(user_id)
            .filter(title__in=set(titles))
            .exclude(likemovie__user_id=user_id)
            .exclude(watchlatermovie__user_id=user_id)
        )
        return [self._to_recommendation_dto(movie) for movie in queryset]

    def get_popular_movies(self, user_id: int, limit: int = 10) -> list[MovieRecommendation]:
        queryset = (
            self._recommendation_queryset(user_id)
            .exclude(likemovie__user_id=user_id)
            .exclude(watchlatermovie__user_id=user_id)
            .order_by('-likes_count', '-watch_later_count', '-created_at')[:limit]
        )
        return [self._to_recommendation_dto(movie) for movie in queryset]

    def replace_cached_recommendations(self, user_id: int, recommendation_date, movie_ids: list[int]) -> None:
        desired_movie_ids = set(movie_ids)

        existing_entries = {
            entry.movie_id: entry
            for entry in RecommendedMovie.objects.filter(
                user_id=user_id,
                recommendation_date=recommendation_date,
            )
        }
        existing_movie_ids = set(existing_entries.keys())

        now = timezone.now()
        entries_to_update: list[RecommendedMovie] = []

        for movie_id, entry in existing_entries.items():
            if movie_id in desired_movie_ids:
                if not entry.is_active or entry.deactivated_at is not None:
                    entry.is_active = True
                    entry.deactivated_at = None
                    entries_to_update.append(entry)
            elif entry.is_active or entry.deactivated_at is None:
                entry.is_active = False
                entry.deactivated_at = now
                entries_to_update.append(entry)

        new_movie_ids = desired_movie_ids - existing_movie_ids

        entries_to_create = [
            RecommendedMovie(
                user_id=user_id,
                movie_id=movie_id,
                recommendation_date=recommendation_date,
                is_active=True,
            )
            for movie_id in new_movie_ids
        ]

        if entries_to_update:
            RecommendedMovie.objects.bulk_update(entries_to_update, ['is_active', 'deactivated_at'])

        if entries_to_create:
            RecommendedMovie.objects.bulk_create(entries_to_create)

    def get_user_activity_summary(self, user_id: int) -> UserActivitySummary:
        user_movies = Movie.objects.filter(Q(likemovie__user_id=user_id) | Q(watchlatermovie__user_id=user_id)).distinct()

        top_genres = list(
            user_movies.values('genres__name').exclude(genres__name__isnull=True).annotate(count=Count('genres__name')).order_by('-count')[:5]
        )
        top_directors = list(
            user_movies.values('directors__full_name')
            .exclude(directors__full_name__isnull=True)
            .annotate(count=Count('directors__full_name'))
            .order_by('-count')[:5]
        )
        top_actors = list(
            user_movies.values('actors__full_name')
            .exclude(actors__full_name__isnull=True)
            .annotate(count=Count('actors__full_name'))
            .order_by('-count')[:5]
        )

        liked_titles = list(
            LikeMovie.objects.filter(user_id=user_id).select_related('movie').order_by('-created_at').values_list('movie__title', flat=True)[:5]
        )
        watch_later_titles = list(
            WatchLaterMovie.objects.filter(user_id=user_id).select_related('movie').order_by('-created_at').values_list('movie__title', flat=True)[:5]
        )

        return UserActivitySummary(
            top_genres=[item['genres__name'] for item in top_genres],
            top_directors=[item['directors__full_name'] for item in top_directors],
            top_actors=[item['actors__full_name'] for item in top_actors],
            liked_titles=liked_titles,
            watch_later_titles=watch_later_titles,
            has_movies=bool(liked_titles or watch_later_titles or top_genres or top_directors or top_actors),
        )

    def _recommendation_queryset(self, user_id: int):
        return (
            Movie.objects.all()
            .with_is_liked(user_id)
            .with_is_watch_later(user_id)
            .with_is_watched(user_id)
            .with_likes_count()
            .with_watch_later_count()
            .annotate(
                genres_names=ArrayAgg(
                    'genres__name',
                    filter=Q(genres__name__isnull=False),
                    distinct=True,
                    order_by=('genres__name',),
                ),
                actors_names=ArrayAgg(
                    'actors__full_name',
                    filter=Q(actors__full_name__isnull=False),
                    distinct=True,
                    order_by=('actors__full_name',),
                ),
                directors_names=ArrayAgg(
                    'directors__full_name',
                    filter=Q(directors__full_name__isnull=False),
                    distinct=True,
                    order_by=('directors__full_name',),
                ),
                writers_names=ArrayAgg(
                    'writers__full_name',
                    filter=Q(writers__full_name__isnull=False),
                    distinct=True,
                    order_by=('writers__full_name',),
                ),
                languages_names=ArrayAgg(
                    'languages__name',
                    filter=Q(languages__name__isnull=False),
                    distinct=True,
                    order_by=('languages__name',),
                ),
                countries_names=ArrayAgg(
                    'countries__name',
                    filter=Q(countries__name__isnull=False),
                    distinct=True,
                    order_by=('countries__name',),
                ),
                ratings_data=JSONBAgg(
                    JSONObject(
                        source=F('movie_ratings__source'),
                        value=F('movie_ratings__value'),
                    ),
                    filter=Q(movie_ratings__id__isnull=False),
                    distinct=True,
                    default=Value([], output_field=JSONField()),
                ),
            )
        )

    @staticmethod
    def _to_recommendation_dto(movie: Movie) -> MovieRecommendation:
        genres = getattr(movie, 'genres_names', None) or []
        actors = getattr(movie, 'actors_names', None) or []
        directors = getattr(movie, 'directors_names', None) or []
        writers = getattr(movie, 'writers_names', None) or []
        languages = getattr(movie, 'languages_names', None) or []
        countries = getattr(movie, 'countries_names', None) or []
        ratings = [rating for rating in (getattr(movie, 'ratings_data', None) or []) if rating]

        return MovieRecommendation(
            id=movie.id,
            imdb_id=movie.imdb_id,
            title=movie.title,
            year=movie.year or None,
            released_date=movie.released_date,
            runtime=movie.runtime or None,
            plot=movie.plot or None,
            awards=movie.awards or None,
            poster=movie.poster or None,
            metascore=movie.metascore or None,
            imdb_rating=movie.imdb_rating or None,
            imdb_votes=movie.imdb_votes or None,
            type=movie.type or None,
            total_seasons=movie.total_seasons or None,
            created_at=movie.created_at,
            genres=[GenreDTO(name) for name in genres],
            actors=[ActorDTO(name) for name in actors],
            directors=[DirectorDTO(name) for name in directors],
            writers=[WriterDTO(name) for name in writers],
            ratings=[
                RatingDTO(source=rating.get('source'), value=rating.get('value'))
                for rating in ratings
                if rating.get('source') is not None or rating.get('value') is not None
            ],
            languages=[LanguageDTO(name) for name in languages],
            countries=[CountryDTO(name) for name in countries],
            is_liked=bool(getattr(movie, 'is_liked', False)),
            likes_count=int(getattr(movie, 'likes_count', 0) or 0),
            is_watch_later=bool(getattr(movie, 'is_watch_later', False)),
            watch_later_count=int(getattr(movie, 'watch_later_count', 0) or 0),
            is_watched=bool(getattr(movie, 'is_watched', False)),
        )


class GenreRepository:
    def get_all(self) -> list[GenreDTO]:
        genres = Genre.objects.values_list('name', flat=True).distinct()
        return [GenreDTO(name=g) for g in genres]


class TopMoviesRepository(RecommendationRepository):
    def get_latest_generated_at(self):
        return TopMovie.objects.order_by('-generated_at').values_list('generated_at', flat=True).first()

    def replace_top_movies(self, movie_ids: list[int]):
        generated_at = timezone.now()
        seen_ids = set()
        ordered_unique_ids: list[int] = []
        for movie_id in movie_ids:
            if movie_id in seen_ids:
                continue
            seen_ids.add(movie_id)
            ordered_unique_ids.append(movie_id)

        with transaction.atomic():
            TopMovie.objects.all().delete()
            entries = [TopMovie(movie_id=movie_id, position=idx, generated_at=generated_at) for idx, movie_id in enumerate(ordered_unique_ids)]
            TopMovie.objects.bulk_create(entries)

        return generated_at

    def get_top_movies(self, user_id: int | None) -> list[MovieRecommendation]:
        generated_at = self.get_latest_generated_at()
        if generated_at is None:
            return []

        movie_ids = list(TopMovie.objects.filter(generated_at=generated_at).order_by('position').values_list('movie_id', flat=True))
        if not movie_ids:
            return []

        order_case = Case(
            *[When(id=movie_id, then=idx) for idx, movie_id in enumerate(movie_ids)],
            default=len(movie_ids),
            output_field=IntegerField(),
        )

        queryset = self._recommendation_queryset(user_id).filter(id__in=movie_ids).annotate(_top_order=order_case).order_by('_top_order')
        return [self._to_recommendation_dto(movie) for movie in queryset]
