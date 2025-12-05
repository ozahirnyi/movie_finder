from __future__ import annotations

from rest_framework import serializers


class CollectionMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    imdb_id = serializers.CharField(allow_null=True, allow_blank=True)
    poster = serializers.CharField(allow_null=True, allow_blank=True)
    year = serializers.CharField(allow_null=True, allow_blank=True)


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_public = serializers.BooleanField()
    owner_id = serializers.IntegerField()
    owner_email = serializers.EmailField(allow_null=True)
    movies_count = serializers.IntegerField()
    is_subscribed = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class CollectionCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000, allow_blank=True, required=False, default='')
    is_public = serializers.BooleanField(required=False, default=False)
    movie_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False,
        allow_empty=True,
    )


class CollectionUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(max_length=1000, allow_blank=True, required=False)
    is_public = serializers.BooleanField(required=False)
    movie_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        required=False,
        allow_empty=True,
    )


class EmptySerializer(serializers.Serializer):
    pass
