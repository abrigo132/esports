from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель пользователя
    """

    class Role(models.TextChoices):
        PLAYER = "player", "Игрок"
        MANAGER = "manager", "Менеджер"
        INFLUENCER = "influencer", "Блогер"
        MARKETER = "marketer", "Маркетолог"
        COPYWRITER = "copywriter", "Копирайтер"
        OTHER = "other", "другое"

    # Базовые данные
    nickname = models.CharField(max_length=50, unique=True, verbose_name="Никнэйм")
    description = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name="Описание"
    )
    first_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Фамилия"
    )
    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.PLAYER, verbose_name="роль"
    )

    # Дополнительные данные
    avatar = models.ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="Аватарка"
    )
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    country = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Страна"
    )

    # Киберспортивные данные

    favorite_games = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Любимые игры"
    )
    main_game = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Основная игра"
    )
    rank = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ранг")
    team = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Команда"
    )

    # Социальные сети

    steam = models.URLField(blank=True, null=True, verbose_name="Steam")
    twitch = models.URLField(blank=True, null=True, verbose_name="Twitch")
    youtube = models.URLField(blank=True, null=True, verbose_name="Youtube")

    # Статистика активности

    is_online = models.BooleanField(default=True, verbose_name="Статус")
    last_online = models.DateTimeField(
        blank=True, null=True, verbose_name="Последний онлайн"
    )
    # Указываем related_name для groups и user_permissions
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="custom_user_set",  # Уникальный related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="custom_user_set",  # Уникальный related_name
        related_query_name="user",
    )

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
