from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Bank
from .serializers import BankSerializer
from .permissions import IsOwnerOrReadOnly


class BankView(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
