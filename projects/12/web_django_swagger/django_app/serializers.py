from django.contrib.auth.models import User
from django.core import validators
from drf_yasg import openapi
from rest_framework import serializers
from django_app import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = "__all__"  # ["title", "description"]


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = "__all__"  # ['id', 'user', 'title', 'is_pay']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = "__all__"  # ['id', 'user', 'title', 'is_pay']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
