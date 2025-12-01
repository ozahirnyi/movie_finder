from rest_framework import serializers

from .models import (
    Actor,
    Country,
    Director,
    Genre,
    Language,
    Movie,
    Rating,
    WatchLaterMovie,
    Writer,
)


class LikesWatchLaterSerializer(serializers.Serializer):
    likes_count = serializers.IntegerField(read_only=True, default=0)
    is_liked = serializers.BooleanField(read_only=True, default=False)
    watch_later_count = serializers.IntegerField(read_only=True, default=0)
    is_watch_later = serializers.BooleanField(read_only=True, default=False)


class StructuresSerializer(serializers.Serializer):
    genres = serializers.ListField(child=serializers.CharField())


class EmptySerializer(serializers.Serializer):
    pass


class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class ActorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('full_name',)


class DirectorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('full_name',)


class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('source', 'value')


class LanguageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name',)


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)


class WriterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ('full_name',)


class MovieModelSerializer(serializers.ModelSerializer, LikesWatchLaterSerializer):
    genres = GenreModelSerializer(many=True, read_only=True)
    actors = ActorModelSerializer(many=True, read_only=True)
    directors = DirectorModelSerializer(many=True, read_only=True)
    ratings = RatingModelSerializer(many=True, read_only=True)
    languages = LanguageModelSerializer(many=True, read_only=True)
    countries = CountryModelSerializer(many=True, read_only=True)
    writers = WriterModelSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'imdb_id',
            'title',
            'year',
            'released_date',
            'runtime',
            'plot',
            'languages',
            'countries',
            'awards',
            'poster',
            'metascore',
            'ratings',
            'imdb_rating',
            'imdb_votes',
            'type',
            'total_seasons',
            'writers',
            'genres',
            'actors',
            'directors',
            'is_liked',
            'likes_count',
            'is_watch_later',
            'watch_later_count',
            'created_at',
        )


class GenreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)


class ActorSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True)


class DirectorSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True)


class RatingSerializer(serializers.Serializer):
    source = serializers.CharField(max_length=255, required=True)
    value = serializers.CharField(max_length=255, required=True)


class LanguageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)


class WriterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True)


class MovieSerializer(LikesWatchLaterSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255, required=True)
    year = serializers.CharField(max_length=255, required=False)
    released_date = serializers.DateField(required=False)
    runtime = serializers.CharField(max_length=255, required=False)
    plot = serializers.CharField(max_length=255, required=False)
    awards = serializers.CharField(max_length=255, required=False)
    poster = serializers.CharField(max_length=255, required=False)
    metascore = serializers.CharField(max_length=255, required=False)
    imdb_rating = serializers.CharField(max_length=255, required=False)
    imdb_votes = serializers.CharField(max_length=255, required=False)
    type = serializers.CharField(max_length=255, required=False)
    total_seasons = serializers.CharField(max_length=255, required=False)
    imdb_id = serializers.CharField(max_length=255, required=False)
    writers = WriterSerializer(many=True, required=False)
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    countries = CountrySerializer(many=True, read_only=True)
    writers = WriterSerializer(many=True, read_only=True)


class WatchLaterListSerializer(MovieModelSerializer):
    pass


class MovieRecommendationSerializer(MovieSerializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField(allow_null=True)


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


class WatchLaterStatisticsRatingSerializer(serializers.Serializer):
    ratings_9_plus = serializers.IntegerField()
    ratings_8_to_9 = serializers.IntegerField()
    ratings_7_to_8 = serializers.IntegerField()
    ratings_6_to_7 = serializers.IntegerField()
    ratings_5_to_6 = serializers.IntegerField()
    ratings_below_5 = serializers.IntegerField()


class WatchLaterStatisticsGenreSerializer(serializers.Serializer):
    genre = serializers.CharField(max_length=255)
    count = serializers.IntegerField()


class WatchLaterStatisticsSerializer(serializers.Serializer):
    ratings = WatchLaterStatisticsRatingSerializer()
    genres = WatchLaterStatisticsGenreSerializer(many=True)


class FindMovieAiSearchViewRequestSerializer(serializers.Serializer):
    expression = serializers.CharField(max_length=255, required=True, allow_blank=False)


class FindMovieSearchViewRequestSerializer(serializers.Serializer):
    expression = serializers.CharField(max_length=255, required=True, allow_blank=False)
