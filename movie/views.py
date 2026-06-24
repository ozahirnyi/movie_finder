import json
import logging
from concurrent.futures import ThreadPoolExecutor
from queue import Empty, Queue
from threading import Thread

from django.db import IntegrityError, close_old_connections
from django.db.models import Case, Count, Max, Value, When
from django.http import StreamingHttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, permissions, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.exceptions import AiSearchLimitExceeded
from auth_app.repositories import UserRepository
from movie_finder_django.metrics import ai_search_limit_hit_total, ai_search_used_total
from throttling.throttling import (
    AiSearchForwardedThrottle,
    AiSearchIpThrottle,
    AiSearchUaThrottle,
    RegularSearchForwardedThrottle,
    RegularSearchIpThrottle,
    RegularSearchUaThrottle,
    consume_guest_ai_search_quota,
)

from .dataclasses import UserContext
from .errors import AddLikeError, AddWatchedError, AiSearchLimitError
from .filters import MovieFilter, WatchLaterFilter
from .models import LikeMovie, Movie, WatchedMovie, WatchLaterMovie
from .paginations import MoviesPagination
from .renderers import STREAM_RENDERERS
from .serializers import (
    EmptySerializer,
    FindMovieAiSearchViewRequestSerializer,
    FindMovieSearchViewRequestSerializer,
    MovieModelSerializer,
    MovieRecommendationSerializer,
    MovieSerializer,
    StructuresSerializer,
    WatchLaterCreateSerializer,
    WatchLaterListSerializer,
    WatchLaterStatisticsSerializer,
)
from .services import GenreService, MovieRecommendationService, MovieService, TopMoviesService
from .trailer import lookup_trailer_video_id

AI_STREAM_RESOLVE_MAX_WORKERS = 2
AI_STREAM_RESOLVE_POLL_INTERVAL_SECONDS = 0.05


def _consume_ai_search_quota(request):
    if not request.user.is_authenticated:
        if consume_guest_ai_search_quota(request):
            ai_search_used_total.labels(tier_code='guest').inc()
            return
        ai_search_limit_hit_total.labels(tier_code='guest').inc()
        raise AiSearchLimitError

    user_repository = UserRepository()
    try:
        user_repository.consume_ai_search_quota(request.user)
        ai_search_used_total.labels(tier_code=request.user.account_tier.code).inc()
    except AiSearchLimitExceeded:
        ai_search_limit_hit_total.labels(tier_code=request.user.account_tier.code).inc()
        raise AiSearchLimitError


def _stream_resolved_ai_movies(
    movie_service,
    expression: str,
    initiator_id: int,
    *,
    max_workers: int = AI_STREAM_RESOLVE_MAX_WORKERS,
    poll_interval_seconds: float = AI_STREAM_RESOLVE_POLL_INTERVAL_SECONDS,
):
    queue = Queue()
    producer_done = object()

    def produce_ai_movies():
        try:
            for index, ai_movie in enumerate(movie_service.stream_movies_from_ai(expression)):
                queue.put((index, ai_movie))
        except Exception as exc:
            queue.put(exc)
        finally:
            queue.put(producer_done)

    def resolve_safe(index, ai_movie):
        try:
            return index, ai_movie, movie_service.resolve_ai_movie(ai_movie, initiator_id)
        except Exception as exc:
            logging.getLogger(__name__).warning('AI streamed movie resolve failed: title=%r error=%s', ai_movie.title, exc)
            return index, ai_movie, None
        finally:
            close_old_connections()

    producer = Thread(target=produce_ai_movies, daemon=True)
    producer.start()

    pending = set()
    producer_finished = False

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while not producer_finished or pending:
            try:
                item = queue.get(timeout=poll_interval_seconds)
            except Empty:
                item = None

            if item is producer_done:
                producer_finished = True
            elif isinstance(item, Exception):
                raise item
            elif item is not None:
                index, ai_movie = item
                pending.add(executor.submit(resolve_safe, index, ai_movie))

            completed = {future for future in pending if future.done()}
            for future in completed:
                pending.remove(future)
                yield future.result()


class MovieView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieModelSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.request.user.id if self.request.user.is_authenticated else None
        return Movie.objects.with_is_liked(user_id).with_is_watch_later(user_id).with_is_watched(user_id).with_likes_count().with_watch_later_count()


class MovieLikeView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmptySerializer
    queryset = LikeMovie.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data or {})
        serializer.is_valid(raise_exception=True)
        try:
            LikeMovie.objects.create(user=self.request.user, movie_id=kwargs.get('id'))
        except IntegrityError:
            raise AddLikeError

        return Response(status=status.HTTP_201_CREATED)


class MovieUnlikeView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = LikeMovie.objects.all()
    serializer_class = EmptySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data or {})
        serializer.is_valid(raise_exception=True)
        LikeMovie.objects.filter(user=self.request.user, movie_id=kwargs.get('id')).delete()

        return Response(status=status.HTTP_200_OK)


class MovieWatchedView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmptySerializer
    queryset = WatchedMovie.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data or {})
        serializer.is_valid(raise_exception=True)
        try:
            WatchedMovie.objects.create(user=self.request.user, movie_id=kwargs.get('id'))
        except IntegrityError:
            raise AddWatchedError

        return Response(status=status.HTTP_201_CREATED)


class MovieUnwatchedView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WatchedMovie.objects.all()
    serializer_class = EmptySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data or {})
        serializer.is_valid(raise_exception=True)
        WatchedMovie.objects.filter(user=self.request.user, movie_id=kwargs.get('id')).delete()

        return Response(status=status.HTTP_200_OK)


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='ordering',
            description='Comma-separated list of ordering fields. Prefix with `-` for descending order.',
            required=False,
            type=str,
            enum=[
                '-imdb_id',
                'imdb_id',
                '-title',
                'title',
                '-genre',
                'genre',
                '-year',
                'year',
                '-likes_count',
                'likes_count',
                '-imdb_rating',
                'imdb_rating',
                '-created_at',
                'created_at',
            ],
        ),
    ]
)
class MoviesListView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieModelSerializer
    pagination_class = MoviesPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['title']
    ordering_fields = ['imdb_id', 'title', 'genre', 'year', 'likes_count', 'imdb_rating', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        user_id = self.request.user.id if self.request.user.is_authenticated else None
        return (
            Movie.objects.all()
            .with_is_liked(user_id)
            .with_is_watch_later(user_id)
            .with_is_watched(user_id)
            .with_likes_count()
            .with_watch_later_count()
        )


class MoviesSearchView(APIView):
    permission_classes = [permissions.AllowAny]
    throttle_classes = [
        RegularSearchUaThrottle,
        RegularSearchIpThrottle,
        RegularSearchForwardedThrottle,
    ]

    @extend_schema(
        request=FindMovieSearchViewRequestSerializer,
        responses={status.HTTP_200_OK: MovieSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        input_serializer = FindMovieSearchViewRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        movie_service = MovieService()
        imdb_movies = movie_service.get_movies_from_imdb(input_serializer.data.get('expression'))
        omdb_movies = movie_service.search_movies_in_omdb_from_imdb_list(imdb_movies, self.request.user.id)
        serialized_movies = MovieSerializer(omdb_movies, many=True)
        return Response(serialized_movies.data, status=status.HTTP_200_OK)


class MoviesAiSearchView(APIView):
    permission_classes = [permissions.AllowAny]

    throttle_classes = [
        AiSearchUaThrottle,
        AiSearchIpThrottle,
        AiSearchForwardedThrottle,
    ]

    @extend_schema(
        request=FindMovieAiSearchViewRequestSerializer,
        responses={status.HTTP_200_OK: MovieSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        input_serializer = FindMovieAiSearchViewRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        try:
            _consume_ai_search_quota(request)
        except AiSearchLimitError:
            raise
        try:
            movie_service = MovieService()
            expression = input_serializer.data.get('expression') or ''
            initiator_id = request.user.id if request.user.is_authenticated else None
            ai_movies = movie_service.get_movies_from_ai(expression)
            omdb_movies = movie_service.resolve_ai_search(ai_movies, initiator_id, expression)
            serialized_movies = MovieSerializer(omdb_movies, many=True)
            return Response(serialized_movies.data, status=status.HTTP_200_OK)
        except Exception as exc:
            logger.exception('movies/ai/search failed: %s', exc)
            return Response(
                {'detail': str(exc)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class MoviesAiSearchStreamView(APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = STREAM_RENDERERS

    throttle_classes = [
        AiSearchUaThrottle,
        AiSearchIpThrottle,
        AiSearchForwardedThrottle,
    ]

    @extend_schema(
        request=FindMovieAiSearchViewRequestSerializer,
        responses={(status.HTTP_200_OK, 'application/x-ndjson'): MovieSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        input_serializer = FindMovieAiSearchViewRequestSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            _consume_ai_search_quota(request)
        except AiSearchLimitError:
            raise

        expression = input_serializer.data.get('expression') or ''
        initiator_id = request.user.id if request.user.is_authenticated else None

        def event_stream():
            movie_service = MovieService()
            ai_movies = []
            resolved_count = 0
            seen_imdb_ids: set[str] = set()

            try:
                for index, ai_movie, movie in _stream_resolved_ai_movies(
                    movie_service,
                    expression,
                    initiator_id,
                ):
                    ai_movies.append(ai_movie)
                    if not movie:
                        continue
                    imdb_id = (movie.imdb_id or '').strip()
                    if imdb_id and imdb_id in seen_imdb_ids:
                        continue
                    if imdb_id:
                        seen_imdb_ids.add(imdb_id)
                    resolved_count += 1
                    payload = MovieSerializer(movie).data
                    yield json.dumps({'event': 'movie', 'index': index, 'data': payload}) + '\n'
            except Exception as exc:
                logger.exception('movies/ai/search/stream AI step failed: %s', exc)
                yield json.dumps({'event': 'error', 'detail': str(exc)}) + '\n'
                return

            if resolved_count == 0 and expression:
                fallback_queries = [movie.title for movie in ai_movies[:3] if movie.title] + [expression]
                for query in fallback_queries:
                    if not query or not query.strip():
                        continue
                    imdb_list = movie_service.get_movies_from_imdb(query.strip())
                    if not imdb_list:
                        continue
                    fallback_movies = movie_service.search_movies_in_omdb_from_imdb_list(
                        imdb_list[:10],
                        initiator_id,
                    )
                    for index, movie in enumerate(fallback_movies):
                        imdb_id = (movie.imdb_id or '').strip()
                        if imdb_id and imdb_id in seen_imdb_ids:
                            continue
                        if imdb_id:
                            seen_imdb_ids.add(imdb_id)
                        movie.match_score = ai_movies[index].match_score if index < len(ai_movies) else 50
                        resolved_count += 1
                        payload = MovieSerializer(movie).data
                        yield json.dumps({'event': 'movie', 'index': index, 'data': payload}) + '\n'
                    break

            yield (
                json.dumps(
                    {
                        'event': 'done',
                        'requested': len(ai_movies),
                        'resolved': resolved_count,
                    }
                )
                + '\n'
            )

        response = StreamingHttpResponse(event_stream(), content_type='application/x-ndjson')
        response['Cache-Control'] = 'no-cache'
        response['X-Accel-Buffering'] = 'no'
        return response


class WatchLaterCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='ordering',
            description='Comma-separated list of ordering fields. Prefix with `-` for descending order.',
            required=False,
            type=str,
            enum=[
                '-imdb_id',
                'imdb_id',
                '-title',
                'title',
                '-genre',
                'genre',
                '-year',
                'year',
                '-likes_count',
                'likes_count',
                '-added_at',
                'added_at',
                '-imdb_rating',
                'imdb_rating',
            ],
        ),
    ]
)
class WatchLaterListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterListSerializer
    pagination_class = MoviesPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = WatchLaterFilter
    search_fields = ['title']
    ordering_fields = ['imdb_id', 'title', 'genre', 'year', 'added_at', 'imdb_rating', 'is_watched']
    ordering = ['is_watched', '-added_at']

    def get_queryset(self):
        user_id = self.request.user.id
        return (
            Movie.objects.filter(watchlatermovie__user_id=user_id)
            .annotate(added_at=Max('watchlatermovie__created_at'))
            .with_is_liked(user_id)
            .with_is_watch_later(user_id)
            .with_is_watched(user_id)
            .with_likes_count()
            .with_watch_later_count()
        )


class WatchLaterStatisticsView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WatchLaterStatisticsSerializer

    def get(self, request, *args, **kwargs):
        rating_stats = WatchLaterMovie.objects.filter(user=self.request.user).aggregate(
            ratings_9_plus=Count(Case(When(movie__movie_ratings__value__gte='9.0', then=Value(1)))),
            ratings_8_to_9=Count(Case(When(movie__movie_ratings__value__gte='8.0', movie__movie_ratings__value__lt='9.0', then=Value(1)))),
            ratings_7_to_8=Count(Case(When(movie__movie_ratings__value__gte='7.0', movie__movie_ratings__value__lt='8.0', then=Value(1)))),
            ratings_6_to_7=Count(Case(When(movie__movie_ratings__value__gte='6.0', movie__movie_ratings__value__lt='7.0', then=Value(1)))),
            ratings_5_to_6=Count(Case(When(movie__movie_ratings__value__gte='5.0', movie__movie_ratings__value__lt='6.0', then=Value(1)))),
            ratings_below_5=Count(Case(When(movie__movie_ratings__value__lt='5.0', then=Value(1)))),
        )
        genres_stats = (
            WatchLaterMovie.objects.filter(user=self.request.user)
            .exclude(movie__genres__name__isnull=True)
            .values('movie__genres__name')
            .annotate(count=Count('movie__genres'))
            .order_by('-count')
        )
        genres_data = [{'genre': g['movie__genres__name'], 'count': g['count']} for g in genres_stats]
        serializer = self.get_serializer(
            data={
                'ratings': rating_stats,
                'genres': genres_data,
            }
        )
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)


class WatchLaterDestroyView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmptySerializer
    queryset = WatchLaterMovie.objects.all()

    def delete(self, request, *args, **kwargs):
        WatchLaterMovie.objects.filter(user_id=self.request.user.id, movie_id=kwargs.get('pk')).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class StructuresListView(generics.GenericAPIView):
    serializer_class = StructuresSerializer

    def get(self, request, *args, **kwargs):
        service = GenreService()
        genres = service.get_all_genres()
        genre_names = [genre.name for genre in genres]
        data = {'genres': genre_names}
        serializer = self.get_serializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviesRecommendationsView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MovieRecommendationSerializer

    def get(self, request, *args, **kwargs):
        recommendation_service = MovieRecommendationService()
        user_context = UserContext(id=request.user.id)
        recommended_movies = recommendation_service.get_recommended_movies(user_context)
        serializer = self.get_serializer(recommended_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopMoviesView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieRecommendationSerializer

    def get(self, request, *args, **kwargs):
        top_movies_service = TopMoviesService()
        user_id = request.user.id if request.user.is_authenticated else None
        movies = top_movies_service.get_top_movies(user_id)
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieTrailerView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        title = request.query_params.get('title', '')
        year = request.query_params.get('year')
        imdb_id = request.query_params.get('imdb_id')
        video_id = lookup_trailer_video_id(title, year, imdb_id)
        if not video_id:
            return Response({'videoId': None}, status=status.HTTP_404_NOT_FOUND)
        return Response({'videoId': video_id}, status=status.HTTP_200_OK)
