from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters import rest_framework as filters

from .models import User
from .serializers import (
    UserSerializer,
    UserSignUpSerializer,
    ProfileSerializer,
    ChangePasswordSerializer,
)
from .services import FilterUsersList


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    Просмотр профиля и обновление данных
    """

    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class SignUpView(generics.CreateAPIView):
    """
    Регистрация пользователей
    """

    serializer_class = UserSignUpSerializer


class SocialLoginView(generics.GenericAPIView):
    """
    Выпуск JWT для пользователей, которые проходят стороннюю аутентификацию
    """

    def post(self, request: Request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return Response(data={"error": "User is not authenticated"}, status=401)

        refresh = RefreshToken.for_user(user=user)
        access_token = str(RefreshToken.access_token)
        refresh_token = str(refresh)

        return Response(
            data={
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": {"id": user.id, "email": user.email, "username": user.username},
            }
        )


class ListUsersView(generics.ListAPIView):
    """
    Просмотр всех пользователей и фильтрация для глобального поиска
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = FilterUsersList
    permission_classes = [IsAuthenticated]


class ChangePasswordView(generics.UpdateAPIView):
    """
    Вью для смены пароля в личном кабинете
    """

    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": "Wrong old password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.set_password(serializer.data.get("new_password"))
            user.save()

            return Response(
                {"message": "Password was updated"}, status=status.HTTP_200_OK
            )
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
