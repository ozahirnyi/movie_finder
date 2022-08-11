from django.contrib import admin
from django.urls import path

from views.auth_views import LoginView, RegistrationView
from views.finder_views import FindMovieView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('find_movie/<str:expression>/', FindMovieView.as_view(), name='find_movie'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='register'),
]
