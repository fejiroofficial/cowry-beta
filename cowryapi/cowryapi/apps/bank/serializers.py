from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Bank, BankMembers, Payment


class BankSerializer(serializers.ModelSerializer):
    created_by_id = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Bank
        fields = ['name', 'set_amount', 'set_period', 'created_by_id',]
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Bank.objects.create_bank(**validated_data)


class BankCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankMembers
        fields = '__all__'
    
    def create(self, validated_data):
        return BankMembers.objects.join_bank(**validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
    
    def create(self, validated_data):
        return Payment.objects.create(**validated_data)
