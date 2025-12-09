from django.contrib.auth import get_user_model
from django.db import models


class Collection(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    design = models.CharField(max_length=255, blank=True, default='')
    is_public = models.BooleanField(default=False)
    movies = models.ManyToManyField('movie.Movie', through='CollectionMovie', related_name='collections')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.name} ({self.owner_id})'


class CollectionMovie(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='collection_movies')
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='movie_collections')
    position = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position', 'added_at', 'id']
        constraints = [
            models.UniqueConstraint(fields=['collection', 'movie'], name='collection_movie_unique'),
        ]

    def __str__(self) -> str:
        return f'{self.collection_id}:{self.movie_id}'


class CollectionSubscription(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='subscriptions')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='collection_subscriptions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['collection', 'user'], name='collection_subscription_unique'),
        ]

    def __str__(self) -> str:
        return f'{self.collection_id}:{self.user_id}'
