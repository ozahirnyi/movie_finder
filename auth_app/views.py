from allauth.socialaccount.providers.google.views import oauth2_login
from django.conf import settings
from django.views import View
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ChangePasswordSerializer,
    PersonalInfoSerializer,
    SignUpSerializer,
)


def _allowed_oauth_return_origins() -> set[str]:
    origins = {
        settings.FRONTEND_URL.rstrip('/'),
        'http://localhost:3000',
        'http://127.0.0.1:3000',
    }
    for origin in getattr(settings, 'LOCAL_FRONTEND_ORIGINS', []):
        origins.add(origin.rstrip('/'))
    return origins


class GoogleLoginStartView(View):
    """Store frontend origin in session so OAuth redirect returns to the same host (localhost vs 127.0.0.1)."""

    def get(self, request, *args, **kwargs):
        return_origin = request.GET.get('return_origin', '').strip().rstrip('/')
        if return_origin in _allowed_oauth_return_origins():
            request.session['oauth_return_origin'] = return_origin
        return oauth2_login(request)


class SignUpApiView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SignUpSerializer


class ChangePasswordAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def patch(self, request, *args, **kwargs):
        serializer_data = request.data

        serializer = self.serializer_class(
            request.user,
            data=serializer_data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonalInfoAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonalInfoSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
