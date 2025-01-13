from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "nickname",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "description",
            "country",
            "city",
            "favorite_games",
            "main_game",
            "rank",
            "team",
            "steam",
            "twitch",
            "youtube",
            "last_online",
            "is_online",
        ]
