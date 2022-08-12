from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from reviews.models import Comment, Review

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    """Сериализатор регистрации юзера."""

    class Meta:
        model = User
        fields = ('email', 'username')


class TokenObtainSerializer(TokenObtainPairSerializer):
    """Сериализатор получения токена по запросу."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['confirmation_code'] = self.fields['password']


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date', )
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', )
        model = Comment