from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api_auth.views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
from api.views import FindMovieView

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
]
