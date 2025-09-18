from .ai_find_movie import FindMovieAiClient
from .dataclasses import AiMovie, ImdbMovie, OmdbMovie
from .repositories import MovieRepository


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies_from_imdb(self, expression: str) -> list[ImdbMovie]:
        return self.movie_repository.get_movies_from_imdb(expression)

    def get_movie_from_omdb_by_expression(self, title: str) -> OmdbMovie:
        return self.movie_repository.get_movie_from_omdb_by_expression(title)

    def search_movies_in_omdb(self, movie_titles: list[str], initiator_id: int) -> list[OmdbMovie]:
        return self.movie_repository.search_movies_in_omdb(movie_titles, initiator_id)

    @staticmethod
    def get_movies_from_ai(expression: str) -> list[AiMovie]:
        return FindMovieAiClient(expression).find_movies()
