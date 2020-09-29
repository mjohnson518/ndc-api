from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from pages.models import NDC
from .permissions import IsAuthorOrReadOnly
from .serializers import NDCSerializer, UserSerializer


class NDCViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = NDC.objects.all()
    serializer_class = NDCSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
