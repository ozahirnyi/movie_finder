from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Dict, List


@dataclass
class Rating:
    source: str
    value: str


@dataclass
class Actor:
    full_name: str


@dataclass
class Genre:
    name: str


@dataclass
class Director:
    full_name: str


@dataclass
class Writer:
    full_name: str


@dataclass
class Country:
    name: str


@dataclass
class Language:
    name: str


@dataclass
class OmdbMovie:
    title: str
    year: str | None = None
    released_date: date | None = None
    runtime: str | None = None
    genres: list[Genre] | None = None
    directors: list[Director] | None = None
    writers: list[Writer] | None = None
    actors: list[Actor] | None = None
    plot: str | None = None
    languages: list[Language] | None = None
    countries: list[Country] | None = None
    awards: str | None = None
    poster: str | None = None
    ratings: List[Rating] | None = None
    metascore: str | None = None
    imdb_rating: str | None = None
    imdb_votes: str | None = None
    imdb_id: str | None = None
    type: str | None = None
    total_seasons: str | None = None
    id: int | None = None


@dataclass
class AiMovie:
    title: str
    match_score: int = 0

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AiMovie':
        if not isinstance(data, dict):
            raise TypeError(f'AiMovie.from_dict expects dict, got {type(data)}')

        return cls(
            title=data.get('title', ''),
            match_score=data.get('match_score', 0),
        )


@dataclass
class ImdbMovie:
    title: str
    imdb_id: str
    poster: str
    year: str
    type: str


@dataclass
class MovieRecommendation:
    id: int
    imdb_id: str | None
    title: str
    year: str | None
    released_date: date | None
    runtime: str | None
    plot: str | None
    awards: str | None
    poster: str | None
    metascore: str | None
    imdb_rating: str | None
    imdb_votes: str | None
    type: str | None
    total_seasons: str | None
    created_at: datetime | None
    genres: list[Genre]
    actors: list[Actor]
    directors: list[Director]
    writers: list[Writer]
    ratings: List[Rating]
    languages: list[Language]
    countries: list[Country]
    is_liked: bool
    likes_count: int
    is_watch_later: bool
    watch_later_count: int


@dataclass
class UserContext:
    id: int


@dataclass
class UserActivitySummary:
    top_genres: List[str]
    top_directors: List[str]
    top_actors: List[str]
    liked_titles: List[str]
    watch_later_titles: List[str]
    has_movies: bool

    @property
    def has_activity(self) -> bool:
        return self.has_movies or any(
            (
                self.top_genres,
                self.top_directors,
                self.top_actors,
                self.liked_titles,
                self.watch_later_titles,
            )
        )
