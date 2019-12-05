from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Bank


class BankSerializer(serializers.ModelSerializer):
    created_by_id = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Bank
        fields = ['name', 'set_amount', 'set_period', 'created_by_id',]
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Bank.objects.create_bank(**validated_data)

