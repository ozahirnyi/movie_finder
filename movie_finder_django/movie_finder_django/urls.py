from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import FindMovieView, WatchLaterListView, WatchLaterDestroyView, WatchLaterCreateView, MovieView, \
    MovieUnlikeView, MovieLikeView
from api_auth.views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView, ChangePasswordAPIView


urlpatterns = [
    # Auth
    path('login/', LoginAPIView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', RegistrationAPIView.as_view(), name='register'),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('user/change_password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('admin/', admin.site.urls),

    # Finder
    path('movie/<int:id>/', MovieView.as_view(), name='movie'),
    path('movie/<int:id>/like/', MovieLikeView.as_view(), name='movie_like'),
    path('movie/<int:id>/unlike/', MovieUnlikeView.as_view(), name='movie_unlike'),
    path('find_movie/<str:expression>/', FindMovieView.as_view(), name='find_movie'),
    path('watch_later/list/', WatchLaterListView.as_view(), name='watch_later_list'),
    path('watch_later/create/', WatchLaterCreateView.as_view(), name='watch_later_create'),
    path('watch_later/<int:pk>/destroy/', WatchLaterDestroyView.as_view(), name='watch_later_destroy'),
]
