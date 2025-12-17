import django_filters
from django.db import models
from django.db.models import Case, FloatField, When
from django.db.models.functions import Cast

from .models import Movie


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(method='filter_title')
    genres = django_filters.CharFilter(field_name='genres__name', lookup_expr='icontains')
    year = django_filters.CharFilter(lookup_expr='icontains')
    imdb_id = django_filters.CharFilter(lookup_expr='exact')
    rating_min = django_filters.NumberFilter(method='filter_rating_min')
    rating_max = django_filters.NumberFilter(method='filter_rating_max')

    class Meta:
        model = Movie
        fields = ['imdb_id', 'title', 'genres', 'year']

    @staticmethod
    def filter_title(queryset, name, value):  # noqa: ARG002
        if not value:
            return queryset
        return queryset.filter(models.Q(title__icontains=value) | models.Q(title_ua__icontains=value))

    @staticmethod
    def _with_numeric_rating(queryset):
        return queryset.annotate(
            imdb_rating_value=Case(
                When(imdb_rating__regex=r'^\d+(\.\d+)?$', then=Cast('imdb_rating', FloatField())),
                default=None,
                output_field=FloatField(),
            )
        )

    def filter_rating_min(self, queryset, name, value):  # noqa: ARG002
        if value is None:
            return queryset
        queryset = self._with_numeric_rating(queryset)
        return queryset.filter(imdb_rating_value__gte=value)

    def filter_rating_max(self, queryset, name, value):  # noqa: ARG002
        if value is None:
            return queryset
        queryset = self._with_numeric_rating(queryset)
        return queryset.filter(imdb_rating_value__lte=value)


class WatchLaterFilter(MovieFilter):
    class Meta:
        model = Movie
        fields = {
            'title': ['icontains'],
            'genres__name': ['icontains'],
            'year': ['icontains'],
            'imdb_id': ['exact'],
        }
