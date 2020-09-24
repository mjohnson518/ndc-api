from django.shortcuts import render
from rest_framework import generics
from pages.models import NDC
from .serializers import NDCSerializer


class NDCAPIView(generics.ListAPIView):
    queryset = NDC.objects.all()
    serializer_class = NDCSerializer
