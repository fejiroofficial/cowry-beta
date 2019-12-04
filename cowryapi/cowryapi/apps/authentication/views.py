from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer


class UserCreateView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CustomUserSerializer
