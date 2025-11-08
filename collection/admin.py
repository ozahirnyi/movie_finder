from django.contrib import admin

from .models import Collection, CollectionMovie


class CollectionMovieInline(admin.TabularInline):
    model = CollectionMovie
    extra = 0


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'is_public', 'movies_count', 'created_at')
    search_fields = ('name', 'owner__email')
    list_filter = ('is_public',)
    inlines = [CollectionMovieInline]

    @staticmethod
    def movies_count(obj: Collection) -> int:
        return obj.collection_movies.count()
