from rest_framework import serializers
from .models import Movie, WatchLaterMovie


class LikesWatchLaterSerializer(serializers.Serializer):
    likes_count = serializers.IntegerField(read_only=True, default=0)
    is_liked = serializers.BooleanField(read_only=True, default=False)
    watch_later_count = serializers.IntegerField(read_only=True, default=0)
    is_watch_later = serializers.BooleanField(read_only=True, default=False)


class MovieSerializer(serializers.ModelSerializer, LikesWatchLaterSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "imdb_id",
            "title",
            "year",
            "type",
            "poster",
            "genre",
            "plot",
            "is_liked",
            "likes_count",
            "is_watch_later",
            "watch_later_count",
        )


class WatchLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchLaterMovie
        fields = "__all__"


class WatchLaterListSerializer(serializers.ModelSerializer, LikesWatchLaterSerializer):
    movie = MovieSerializer()

    class Meta:
        model = WatchLaterMovie
        fields = (
            "movie",
            "is_liked",
            "likes_count",
            "is_watch_later",
            "watch_later_count",
        )
        read_only_fields = fields


class WatchLaterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchLaterMovie
        fields = ("id", "movie")
        extra_kwargs = {
            "movie": {"write_only": True},
        }

    def create(self, validated_data):
        validated_data["user"] = self.context["user"]

        return super().create(validated_data)


class InputSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=255, required=True, allow_blank=False)
