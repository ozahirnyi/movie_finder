from django.db import models


class Actor(models.Model):
    fullname = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname


class Movie(models.Model):
    name = models.CharField(max_length=255)
    actors = models.ManyToManyField(to=Actor)

    def __str__(self):
        return self.name
