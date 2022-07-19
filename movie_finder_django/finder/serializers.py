from django.contrib.auth.models import User, Group
from rest_framework import serializers

from finder.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
