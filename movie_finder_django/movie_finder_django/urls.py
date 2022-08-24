from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import FindMovieView, WatchLaterListView, WatchLaterDestroyView, WatchLaterCreateView
from api_auth.views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    # Auth
    path('login/', LoginAPIView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', RegistrationAPIView.as_view(), name='register'),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('admin/', admin.site.urls),

    # Finder
    path('find_movie/<str:expression>/', FindMovieView.as_view(), name='find_movie'),
    path('watch_later/list/', WatchLaterListView.as_view(), name='watch_later_list'),
    path('watch_later/create/', WatchLaterCreateView.as_view(), name='watch_later_create'),
    path('watch_later/<int:pk>/destroy/', WatchLaterDestroyView.as_view(), name='watch_later_destroy'),
]
