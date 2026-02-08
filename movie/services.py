import logging
import textwrap
from datetime import datetime, timedelta
from datetime import timezone as dt_timezone

from django.conf import settings
from django.core.exceptions import BadRequest
from django.utils import timezone

from .ai_find_movie import FindMovieAiClient, RecommendationFindMovieAiClient, SearchFindMovieAiClient, TopMoviesFindMovieAiClient
from .dataclasses import (
    AiMovie,
    ImdbMovie,
    MovieRecommendation,
    OmdbMovie,
    UserActivitySummary,
    UserContext,
)
from .errors import AiResponseError
from .repositories import GenreRepository, MovieRepository, RecommendationRepository, TopMoviesRepository

logger = logging.getLogger(__name__)


class MovieService:
    def __init__(
        self,
        movie_repository: MovieRepository | None = None,
        ai_client: FindMovieAiClient | None = None,
    ):
        self.movie_repository = movie_repository or MovieRepository()
        self.ai_client = ai_client or SearchFindMovieAiClient()

    def get_movies_from_imdb(self, expression: str) -> list[ImdbMovie]:
        provider = getattr(settings, 'MOVIE_SEARCH_PROVIDER', 'omdb')
        try:
            if provider == 'omdb':
                return self.movie_repository.get_movies_from_omdb_search(expression)
            return self.movie_repository.get_movies_from_imdb(expression)
        except Exception as exc:
            logger.warning(
                'Movie search provider %s failed for expression=%r: %s; falling back to DB search',
                provider,
                expression,
                exc,
                exc_info=True,
            )
            results = self.movie_repository.get_movies_from_db_search(expression)
            logger.info(
                'Movie search DB fallback: expression=%r returned %d result(s)',
                expression,
                len(results),
            )
            return results

    def get_movie_from_omdb_by_expression(self, title: str) -> OmdbMovie | None:
        return self.movie_repository.get_movie_from_omdb_by_expression(title)

    def search_movies_in_omdb(self, movie_titles: list[str], initiator_id: int) -> list[OmdbMovie]:
        return self.movie_repository.search_movies_in_omdb(movie_titles, initiator_id)

    def search_movies_in_omdb_from_imdb_list(self, imdb_movies: list[ImdbMovie], initiator_id: int) -> list[OmdbMovie]:
        """Resolve search results by imdb_id first to avoid duplicate Movie rows."""
        return self.movie_repository.search_movies_in_omdb_from_imdb_list(imdb_movies, initiator_id)

    def get_movies_from_ai(self, expression: str) -> list[AiMovie]:
        try:
            return self.ai_client.find_movies(expression)
        except AiResponseError:
            raise BadRequest('AI service returned an invalid response. Please try again later.')


class RecommendationPromptService:
    def build_prompt(self, activity_summary: UserActivitySummary) -> str:
        genre_list = ', '.join(activity_summary.top_genres) or 'varied genres'
        director_list = ', '.join(activity_summary.top_directors) or 'mixed directors'
        actor_list = ', '.join(activity_summary.top_actors) or 'mixed casts'
        liked_list = ', '.join(activity_summary.liked_titles) if activity_summary.liked_titles else 'None'
        watch_later_list = ', '.join(activity_summary.watch_later_titles) if activity_summary.watch_later_titles else 'None'

        prompt = textwrap.dedent(
            f"""
            Viewer profile:
            - Preferred genres: {genre_list}.
            - Directors they often watch: {director_list}.
            - Frequent actors: {actor_list}.
            - Recent likes: {liked_list}.
            - Watch-later list: {watch_later_list}.

            Recommend up to 10 new movies that match their taste. Avoid listing any titles already in the likes or watch-later lists.
            """
        )
        return prompt.strip()


class MovieRecommendationService:
    def __init__(
        self,
        recommendation_repository: RecommendationRepository | None = None,
        movie_repository: MovieRepository | None = None,
        prompt_service: RecommendationPromptService | None = None,
        ai_client: FindMovieAiClient | None = None,
    ):
        self.recommendation_repository = recommendation_repository or RecommendationRepository()
        self.movie_repository = movie_repository or MovieRepository()
        self.prompt_service = prompt_service or RecommendationPromptService()
        self.ai_client = ai_client or RecommendationFindMovieAiClient()

    def get_recommended_movies(self, user_context: UserContext) -> list[MovieRecommendation]:
        today = datetime.now(dt_timezone.utc).date()
        cached_movie_ids = self.recommendation_repository.get_cached_movie_ids(user_context.id, today)
        if cached_movie_ids:
            return self.recommendation_repository.get_movies_by_ids(cached_movie_ids, user_context.id)

        activity_summary = self.recommendation_repository.get_user_activity_summary(user_context.id)
        recommended_movies: list[MovieRecommendation] = []

        if activity_summary.has_activity:
            preference_prompt = self.prompt_service.build_prompt(activity_summary)
            ai_movies = self.ai_client.find_movies(preference_prompt)
            requested_titles = {movie.title for movie in ai_movies if movie.title}
            if requested_titles:
                omdb_movies = self.movie_repository.search_movies_in_omdb(list(requested_titles), user_context.id)
                omdb_titles = {movie.title for movie in omdb_movies if movie.title}
                if omdb_titles:
                    recommended_movies = self.recommendation_repository.get_movies_by_titles(list(omdb_titles), user_context.id)

        if not recommended_movies:
            recommended_movies = self.recommendation_repository.get_popular_movies(user_context.id)

        self.recommendation_repository.replace_cached_recommendations(user_context.id, today, [movie.id for movie in recommended_movies])
        return recommended_movies


class GenreService:
    def __init__(self, genre_repository: GenreRepository | None = None):
        self.genre_repository = genre_repository or GenreRepository()

    def get_all_genres(self):
        return self.genre_repository.get_all()


class TopMoviesService:
    REFRESH_INTERVAL_DAYS = 7
    TOP_MOVIES_PROMPT = (
        'Return a JSON array of up to 10 currently trending and widely loved movies or TV series across genres. '
        'Use only real, already released titles (no upcoming). '
        'Respond with the JSON array of titles only, e.g. ["Dune", "Barbie", "Succession"].'
    )

    def __init__(
        self,
        top_movies_repository: TopMoviesRepository | None = None,
        movie_repository: MovieRepository | None = None,
        recommendation_repository: RecommendationRepository | None = None,
        ai_client: FindMovieAiClient | None = None,
    ):
        self.top_movies_repository = top_movies_repository or TopMoviesRepository()
        self.movie_repository = movie_repository or MovieRepository()
        self.recommendation_repository = recommendation_repository or RecommendationRepository()
        self.ai_client = ai_client or TopMoviesFindMovieAiClient()

    def get_top_movies(self, user_id: int | None = None) -> list[MovieRecommendation]:
        last_generated_at = self.top_movies_repository.get_latest_generated_at()

        if self._should_refresh(last_generated_at):
            refreshed_movies = self._refresh_top_movies(user_id)
            if refreshed_movies:
                return refreshed_movies

        cached_movies = self.top_movies_repository.get_top_movies(user_id)
        if cached_movies:
            return cached_movies

        return self._refresh_top_movies(user_id)

    def force_refresh(self, user_id: int | None = None) -> list[MovieRecommendation]:
        return self._refresh_top_movies(user_id)

    def _refresh_top_movies(self, user_id: int | None) -> list[MovieRecommendation]:
        ai_movies = self.ai_client.find_movies(self.TOP_MOVIES_PROMPT)
        requested_titles = [movie.title for movie in ai_movies if movie.title]
        top_movies: list[MovieRecommendation] = []

        if requested_titles:
            omdb_movies = self.movie_repository.search_movies_in_omdb(requested_titles, initiator_id=0)
            movie_ids = [movie.id for movie in omdb_movies if movie.id is not None]
            if movie_ids:
                self.top_movies_repository.replace_top_movies(movie_ids)
                top_movies = self.top_movies_repository.get_top_movies(user_id)

        if not top_movies:
            fallback_movies = self.recommendation_repository.get_popular_movies(0)
            if fallback_movies:
                self.top_movies_repository.replace_top_movies([movie.id for movie in fallback_movies])
                top_movies = self.top_movies_repository.get_top_movies(user_id)

        return top_movies

    def _should_refresh(self, generated_at) -> bool:
        if generated_at is None:
            return True
        return timezone.now() - generated_at >= timedelta(days=self.REFRESH_INTERVAL_DAYS)
