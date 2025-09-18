import django_filters

from .models import Movie, WatchLaterMovie


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    genres = django_filters.CharFilter(field_name='genres__name', lookup_expr='icontains')
    year = django_filters.CharFilter(lookup_expr='icontains')
    imdb_id = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Movie
        fields = ['imdb_id', 'title', 'genres', 'year']


class WatchLaterFilter(MovieFilter):
    class Meta:
        model = WatchLaterMovie
        fields = {
            'movie__title': ['icontains'],
            'movie__genres__name': ['icontains'],
            'movie__year': ['icontains'],
            'movie__imdb_id': ['exact'],
        }
