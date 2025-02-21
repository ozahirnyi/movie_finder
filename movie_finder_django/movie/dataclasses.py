from dataclasses import dataclass


@dataclass
class ImdbMovie:
    title: str
    imdb_id: str
    poster: str
    year: str
    type: str


@dataclass
class AiMovie:
    title: str
    genre: str
    plot: str
