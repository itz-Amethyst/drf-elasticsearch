
from core.models.user import User
from rest_framework import viewsets

from core.api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()