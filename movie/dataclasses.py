from dataclasses import dataclass
from datetime import date
from typing import List


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


@dataclass
class AiMovie:
    title: str


@dataclass
class ImdbMovie:
    title: str
    imdb_id: str
    poster: str
    year: str
    type: str
