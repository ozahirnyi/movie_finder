from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth_app.views import (
    ChangePasswordAPIView,
    SignUpApiView,
)
from movie.views import (
    MovieLikeView,
    MoviesAiSearchView,
    MoviesListView,
    MoviesRecommendationsView,
    MoviesSearchView,
    MovieUnlikeView,
    MovieView,
    StructuresListView,
    TopMoviesView,
    WatchLaterCreateView,
    WatchLaterDestroyView,
    WatchLaterListView,
    WatchLaterStatisticsView,
)

auth_patterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpApiView.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
]

users_patterns = [
    path(
        'users/change_password/',
        ChangePasswordAPIView.as_view(),
        name='change_password',
    ),
]

admin_patterns = [
    path('admin/', admin.site.urls),
]

watch_later_patterns = [
    path('list/', WatchLaterListView.as_view(), name='watch_later_list'),
    path('create/', WatchLaterCreateView.as_view(), name='watch_later_create'),
    path('statistics/', WatchLaterStatisticsView.as_view(), name='watch_later_statistics'),
    path(
        '<int:pk>/destroy/',
        WatchLaterDestroyView.as_view(),
        name='watch_later_destroy',
    ),
]

movies_patterns = [
    path('movies/', MoviesListView.as_view(), name='movies_list'),
    path('movies/<int:id>/', MovieView.as_view(), name='movie'),
    path('movies/<int:id>/like/', MovieLikeView.as_view(), name='movie_like'),
    path('movies/<int:id>/unlike/', MovieUnlikeView.as_view(), name='movie_unlike'),
    path('movies/search/', MoviesSearchView.as_view(), name='movies_search'),
    path('movies/ai/search/', MoviesAiSearchView.as_view(), name='movies_ai_search'),
    path('movies/recommendations/', MoviesRecommendationsView.as_view(), name='movies_recommendations'),
    path('movies/top/', TopMoviesView.as_view(), name='movies_top'),
    path('watch_later/', include(watch_later_patterns)),
    path('structures/', StructuresListView.as_view(), name='genre-list'),
]

swagger_patterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


collections_patterns = [
    path('', include('collection.urls')),
]

urlpatterns = auth_patterns + users_patterns + admin_patterns + movies_patterns + collections_patterns + swagger_patterns
