from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User
from .services import create_user


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра информации пользователя
    """

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
    """
    Сериализатор для регистрации пользователей
    """

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


class ProfileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для личного кабинета и обновления данных пользователя
    """

    description = serializers.CharField(max_length=1000, required=False)
    first_name = serializers.CharField(max_length=50, required=False)
    last_name = serializers.CharField(max_length=50, required=False)
    role = serializers.CharField(max_length=20, required=False)
    avatar = serializers.ImageField(required=False)
    birth_date = serializers.DateField(required=False)
    city = serializers.CharField(max_length=50, required=False)
    country = serializers.CharField(max_length=50, required=False)
    favorite_games = serializers.CharField(max_length=50, required=False)
    main_game = serializers.CharField(max_length=50, required=False)
    rank = serializers.CharField(max_length=50, required=False)
    team = serializers.CharField(max_length=100, required=False)
    steam = serializers.URLField(required=False)
    twitch = serializers.URLField(required=False)
    youtube = serializers.URLField(required=False)

    class Meta:
        model = User
        fields = [
            "description",
            "first_name",
            "last_name",
            "role",
            "avatar",
            "birth_date",
            "city",
            "country",
            "favorite_games",
            "main_game",
            "rank",
            "team",
            "steam",
            "twitch",
            "youtube",
        ]
        read_only_fields = ["id", "username", "email"]


class ChangePasswordSerializer(serializers.Serializer):
    """
    Сериализатор для смены пароля
    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        try:
            validate_password(value)  # Валидация пароля
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value
