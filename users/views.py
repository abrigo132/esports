from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters import rest_framework as filters

from .models import User
from .serializers import UserSerializer, UserSignUpSerializer
from .services import FilterUsersList


class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer


class SocialLoginView(generics.GenericAPIView):

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
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = FilterUsersList
    permission_classes = [IsAuthenticated]
