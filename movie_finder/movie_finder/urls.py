"""movie_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from finder.views import index, registration, favorites, \
    remove_from_favorites_by_imdb_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', registration, name='registration'),
    path('password-change/', views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password-reset/', views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('favorites/', favorites, name='favorites'),
    path('favorites/<slug:imdb_id>/', remove_from_favorites_by_imdb_id,
         name='favorites')
]
