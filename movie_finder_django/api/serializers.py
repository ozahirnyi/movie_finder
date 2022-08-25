from rest_framework import serializers

from .models import Movie, WatchLaterMovie, LikeMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class WatchLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchLaterMovie
        fields = '__all__'


class WatchLaterListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = WatchLaterMovie
        fields = ('id', 'movie')
        read_only_fields = fields


class WatchLaterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchLaterMovie
        fields = ('id', 'movie')
        extra_kwargs = {
            'movie': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['user'] = self.context['user']

        return super().create(validated_data)
