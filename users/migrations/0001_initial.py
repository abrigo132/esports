# Generated by Django 5.1.4 on 2025-01-12 06:07

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Никнэйм"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=1000, null=True, verbose_name="Описание"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Имя"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Фамилия"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="avatars/",
                        verbose_name="Аватарка",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Город"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Страна"
                    ),
                ),
                (
                    "favorite_games",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Любимые игры",
                    ),
                ),
                (
                    "main_game",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Основная игра",
                    ),
                ),
                (
                    "rank",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Ранг"
                    ),
                ),
                (
                    "team",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Команда"
                    ),
                ),
                ("steam", models.URLField(blank=True, null=True, verbose_name="Steam")),
                (
                    "twitch",
                    models.URLField(blank=True, null=True, verbose_name="Twitch"),
                ),
                (
                    "youtube",
                    models.URLField(blank=True, null=True, verbose_name="Youtube"),
                ),
                ("is_online", models.BooleanField(default=True, verbose_name="Статус")),
                (
                    "last_online",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Последний онлайн"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="custom_user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="custom_user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
