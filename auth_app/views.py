from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ChangePasswordSerializer,
    PersonalInfoSerializer,
    SignUpSerializer,
)


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
