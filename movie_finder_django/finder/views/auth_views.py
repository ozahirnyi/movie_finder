from django.contrib.auth import login
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from serializers import LoginSerializer, RegistrationSerializer


class LoginView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(self.request, user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RegistrationView(GenericAPIView):
    permissions = [permissions.AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
