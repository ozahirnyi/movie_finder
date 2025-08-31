from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth_app.views import (
    ChangePasswordAPIView, SignUpApiView,
)
from movie.views import (
    MovieView,
    MovieLikeView,
    MovieUnlikeView,
    FindMovieView,
    WatchLaterListView,
    WatchLaterCreateView,
    WatchLaterDestroyView,
    FindMovieAiView,
)

auth_patterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", SignUpApiView.as_view(), name="signup"),
    path('accounts/', include('allauth.urls')),
]

users_patterns = [
    path(
        "users/change_password/",
        ChangePasswordAPIView.as_view(),
        name="change_password",
    ),
]

admin_patterns = [
    path("admin/", admin.site.urls),
]

movies_patterns = [
    path("movies/<int:id>/", MovieView.as_view(), name="movie"),
    path("movies/<int:id>/like/", MovieLikeView.as_view(), name="movie_like"),
    path("movies/<int:id>/unlike/", MovieUnlikeView.as_view(), name="movie_unlike"),
    path("find_movie/", FindMovieView.as_view(), name="find_movie"),
    path("find_movie_ai/", FindMovieAiView.as_view(), name="find_movie_ai"),
    path("watch_later/list/", WatchLaterListView.as_view(), name="watch_later_list"),
    path(
        "watch_later/create/", WatchLaterCreateView.as_view(), name="watch_later_create"
    ),
    path(
        "watch_later/<int:pk>/destroy/",
        WatchLaterDestroyView.as_view(),
        name="watch_later_destroy",
    ),
]

swagger_patterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]


urlpatterns = auth_patterns + users_patterns + admin_patterns + movies_patterns + swagger_patterns
