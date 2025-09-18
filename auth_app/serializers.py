from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .errors import ChangePasswordError

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6, write_only=True)
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('A user with that email already exists.')
        return value

    def validate(self, data):
        password = data.get('password')
        try:
            validate_password(password)
        except ValidationError as exc:
            raise serializers.ValidationError({'password': exc.messages})
        return data

    def create(self, validated_data):
        return User.objects.create_user(email=validated_data['email'], password=validated_data['password'])


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    new_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('password',)

    def update(self, instance, validated_data):
        old_password = validated_data.pop('old_password', None)
        new_password = validated_data.pop('new_password', None)

        if instance.check_password(old_password):
            instance.set_password(new_password)
            instance.save(update_fields=['password'])
        else:
            raise ChangePasswordError

        return instance
