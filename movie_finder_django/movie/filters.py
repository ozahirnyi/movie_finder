import django_filters
from .models import Movie, WatchLaterMovie


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    genre = django_filters.CharFilter(lookup_expr="icontains")
    year = django_filters.CharFilter(lookup_expr="icontains")
    imdb_id = django_filters.CharFilter(lookup_expr="exact")

    class Meta:
        model = Movie
        fields = ["imdb_id", "title", "genre", "year"]


class WatchLaterFilter(MovieFilter):
    class Meta:
        model = WatchLaterMovie
        fields = {
            "movie__title": ["icontains"],
            "movie__genre": ["icontains"],
            "movie__year": ["icontains"],
            "movie__imdb_id": ["exact"],
        }
