from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class CollectionPayload:
    owner_id: int
    name: str
    description: str | None = ''
    is_public: bool = False
    movie_ids: list[int] | None = field(default=None)


@dataclass(slots=True)
class CollectionUpdatePayload:
    name: str | None = None
    description: str | None = None
    is_public: bool | None = None
    movie_ids: list[int] | None = field(default=None)


@dataclass(slots=True)
class CollectionMovieDTO:
    id: int
    title: str
    imdb_id: str | None
    poster: str | None
    year: str | None


@dataclass(slots=True)
class CollectionDTO:
    id: int
    name: str
    description: str
    is_public: bool
    owner_id: int
    owner_email: str | None
    movies_count: int
    is_subscribed: bool
    created_at: datetime
    updated_at: datetime


@dataclass(slots=True)
class CollectionListResult:
    items: list[CollectionDTO]
    total_count: int


@dataclass(slots=True)
class CollectionMovieListResult:
    items: list[CollectionMovieDTO]
    total_count: int
