from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from finder.views import FindMovieView, index, registration, favorites, favorites_by_imdb_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('find_movie/<str:expression>/', FindMovieView.as_view(), name='find_movie'),
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
    path('favorites/<slug:imdb_id>/', favorites_by_imdb_id,
         name='favorites')
]
