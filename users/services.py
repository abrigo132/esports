from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

User = get_user_model()


def create_user(username: str, email: str, password: str, role: str) -> User:
    """
    Функция для добавления пользователя в базу данных
    :param username:
    :param email:
    :param password:
    :param role:
    :return:
    """
    user = User.objects.create_user(
        username=username, email=email, password=password, role=role
    )
    return user


class FilterUsersList(filters.FilterSet):
    username = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="icontains")
    city = filters.CharFilter(lookup_expr="icontains")
    first_name = filters.CharFilter(lookup_expr="icontains")
    last_name = filters.CharFilter(lookup_expr="icontains")
    main_game = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["username", "email", "city", "first_name", "last_name", "main_game"]
