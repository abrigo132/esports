from rest_framework import serializers

from .models import User
from .services import create_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
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


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email", "role"]

    def create(self, validate_data: dict) -> User:
        return create_user(
            username=validate_data["username"],
            email=validate_data["email"],
            password=validate_data["password"],
            role=validate_data.get("role", User.Role.PLAYER),
        )

    def validate_role(self, value: str) -> str:
        if not value:
            return User.Role.PLAYER
        if value not in User.Role.values:
            raise serializers.ValidationError(
                f"Недопустимая роль. Допустимые значения: {', '.join(User.Role.values)}"
            )
        return value
