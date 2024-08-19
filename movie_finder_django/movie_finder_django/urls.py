from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from movie.views import (
    MovieView, MovieLikeView, MovieUnlikeView, FindMovieView, WatchLaterListView,
    WatchLaterCreateView, WatchLaterDestroyView, FindMovieAiView
)
from auth_app.views import (
    SignInApiView, SignUpApiView, UserRetrieveUpdateAPIView, ChangePasswordAPIView,
)

urlpatterns = [
    # Auth
    path("signin/", SignInApiView.as_view(), name="signin"),
    path("movie/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("movie/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("signup/", SignUpApiView.as_view(), name="signup"),
    path("user/", UserRetrieveUpdateAPIView.as_view(), name="user"),
    path("user/change_password/", ChangePasswordAPIView.as_view(), name="change_password"),
    path("admin/", admin.site.urls),
    # Finder
    path("movie/<int:id>/", MovieView.as_view(), name="movie"),
    path("movie/<int:id>/like/", MovieLikeView.as_view(), name="movie_like"),
    path("movie/<int:id>/unlike/", MovieUnlikeView.as_view(), name="movie_unlike"),
    path("find_movie/<str:expression>/", FindMovieView.as_view(), name="find_movie"),
    path("find_movie_ai/", FindMovieAiView.as_view(), name="find_movie_ai"),
    path("watch_later/list/", WatchLaterListView.as_view(), name="watch_later_list"),
    path("watch_later/create/", WatchLaterCreateView.as_view(), name="watch_later_create"),
    path(
        "watch_later/<int:pk>/destroy/",
        WatchLaterDestroyView.as_view(),
        name="watch_later_destroy",
    ),
]
