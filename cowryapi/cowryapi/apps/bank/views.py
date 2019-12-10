from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, views, generics
from rest_framework.response import Response
from rest_framework.views import status
from .models import Bank, BankMembers
from .serializers import BankSerializer, BankCustomerSerializer
from .permissions import IsOwnerOrReadOnly


class BankView(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    queryset = Bank.objects.all()
    serializer_class = BankSerializer



class BankCustomerJoinView(generics.CreateAPIView):
    """
    Users can join a bank group /banks/<bank_id>/join
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = BankCustomerSerializer(data={
            'guarantor_name': request.data.get('guarantor_name', ''),
            'guarantor_address': request.data.get('guarantor_address', ''),
            'guarantor_phone': request.data.get('guarantor_phone', ''),
            'bank_group': kwargs['bank_id'],
            'bank_member': request.user.id
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={
                'message': 'Application was submitted. Awaiting confirmation.'
            },
            status=status.HTTP_200_OK
        )

class ApproveCustomerView(generics.RetrieveUpdateAPIView):
    """
    Bank owner can approve a customer  /banks/<bank_id>/join/<join_id>
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BankMembers.objects.all()
    serializer_class = BankCustomerSerializer

    def patch(self, request, *args, **kwargs):
        logged_in_user = request.user
        bank_id = kwargs['bank_id']
        join_id = kwargs['pk']
        get_object_or_404(Bank, id=bank_id, created_by=logged_in_user)
        customer = get_object_or_404(BankMembers, pk=join_id, bank_group=bank_id)
        if customer.is_active is True:
            return Response(
                data={
                    'message': 'This is an approved account'
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        customer.is_active = True
        customer.save()
        return Response(
                data={
                    'message': 'Account approved successfully'
                },
                status=status.HTTP_200_OK
            )
