from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer
from users.models import User


class UserAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name", "email", "artistic_name", "username"]


class AlbumSerializer(serializers.ModelSerializer):
    user = UserAlbumSerializer(read_only=True)

    class Meta:
        model = Album
        fields = "__all__"
