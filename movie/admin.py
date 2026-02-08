from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import path

from .models import Movie, TopMovie
from .services import TopMoviesService


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'imdb_id', 'year', 'type', 'imdb_rating', 'created_at')
    list_filter = ('type', 'year')
    search_fields = ('title', 'imdb_id')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('genres', 'actors', 'directors', 'countries', 'languages', 'writers')
    ordering = ('-created_at',)


@admin.register(TopMovie)
class TopMovieAdmin(admin.ModelAdmin):
    list_display = ('movie', 'position', 'generated_at', 'created_at')
    ordering = ('position',)
    change_list_template = 'admin/movie/topmovie_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('refresh/', self.admin_site.admin_view(self.refresh_top_movies), name='movie_topmovie_refresh'),
        ]
        return custom_urls + urls

    def refresh_top_movies(self, request):
        service = TopMoviesService()
        refreshed = service.force_refresh()
        self.message_user(request, f'Top movies refreshed ({len(refreshed)} items).', messages.SUCCESS)
        return redirect('../')
