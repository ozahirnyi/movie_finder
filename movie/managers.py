from django.db import models


class MovieManager(models.QuerySet):
    def with_is_liked(self, user_id: int):
        from .models import LikeMovie

        return self.annotate(
            is_liked=models.Exists(LikeMovie.objects.filter(user_id=user_id, movie_id=models.OuterRef('pk'))),
        )

    def with_is_watch_later(self, user_id: int):
        from .models import WatchLaterMovie

        return self.annotate(
            is_watch_later=models.Exists(WatchLaterMovie.objects.filter(user_id=user_id, movie_id=models.OuterRef('pk'))),
        )

    def with_likes_count(self):
        return self.annotate(likes_count=models.Count('likemovie', distinct=True))

    def with_watch_later_count(self):
        return self.annotate(watch_later_count=models.Count('watchlatermovie', distinct=True))
