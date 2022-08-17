from django.contrib import admin
from django.urls import path

from api_auth.views import LoginView, RegistrationView
from api.views import FindMovieView

urlpatterns = [
    # Finder
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='register'),

    # Auth
    path('admin/', admin.site.urls),
    path('find_movie/<str:expression>/', FindMovieView.as_view(), name='find_movie'),
]
