from django.db import models
from django.db.models import Value


class MovieManager(models.QuerySet):
    def with_is_liked(self, user_id: int | None):
        from .models import LikeMovie

        if not user_id:
            return self.annotate(is_liked=Value(False, output_field=models.BooleanField()))
        return self.annotate(
            is_liked=models.Exists(LikeMovie.objects.filter(user_id=user_id, movie_id=models.OuterRef('pk'))),
        )

    def with_is_watch_later(self, user_id: int | None):
        from .models import WatchLaterMovie

        if not user_id:
            return self.annotate(is_watch_later=Value(False, output_field=models.BooleanField()))
        return self.annotate(
            is_watch_later=models.Exists(WatchLaterMovie.objects.filter(user_id=user_id, movie_id=models.OuterRef('pk'))),
        )

    def with_is_watched(self, user_id: int | None):
        from .models import WatchedMovie

        if not user_id:
            return self.annotate(is_watched=Value(False, output_field=models.BooleanField()))
        return self.annotate(
            is_watched=models.Exists(WatchedMovie.objects.filter(user_id=user_id, movie_id=models.OuterRef('pk'))),
        )

    def with_likes_count(self):
        return self.annotate(likes_count=models.Count('likemovie', distinct=True))

    def with_watch_later_count(self):
        return self.annotate(watch_later_count=models.Count('watchlatermovie', distinct=True))
