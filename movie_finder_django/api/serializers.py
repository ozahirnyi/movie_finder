from rest_framework import serializers

from .models import Movie, WatchLater


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class WatchLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchLater
        fields = '__all__'


class WatchLaterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchLater
        fields = ('id', 'movie')
        extra_kwargs = {
            'id': {'required': False},
            'movie': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['user'] = self.context['user']

        return super().create(validated_data)
