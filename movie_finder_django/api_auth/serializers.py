from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from api_auth.errors import UserAlreadyExist


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Access denied: wrong username or password.')
        else:
            raise serializers.ValidationError('Both "username" and "password" are required.')

        attrs['user'] = user
        return attrs


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        label="Username",
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
    )

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'password',
        ]

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')

        if username and password:
            User = get_user_model()

            if User.objects.filter(username=username).exists():
                raise UserAlreadyExist

            user = User.objects.create_user(username=username, password=password)
        else:
            raise serializers.ValidationError('Both "username" and "password" are required.')

        return user
