from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
