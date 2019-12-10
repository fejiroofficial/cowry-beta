from django.db import models
from cowryapi.apps.authentication.models import CustomUser

from os import getenv
# Create your models here.

class BankManager(models.Manager):
    def create_bank(self, **kwargs):
        name = kwargs.get(
            'name')
        set_amount = kwargs.get(
            'set_amount')
        set_period = kwargs.get(
            'set_period')
        created_by = kwargs.get(
            'created_by')
        bank = self.model(
            name=name,
            set_amount=set_amount,
            set_period=set_period,
            created_by=created_by
        )
        bank.save()
        return bank


class BankCustomerManager(models.Manager):
    def join_bank(self, **kwargs):
        bank_group = kwargs.get(
            'bank_group')
        bank_member = kwargs.get(
            'bank_member')
        guarantor_name = kwargs.get(
            'guarantor_name')
        guarantor_address = kwargs.get(
            'guarantor_address')
        guarantor_phone = kwargs.get(
            'guarantor_phone')
        bank_customer = self.model(
            bank_group=bank_group,
            bank_member=bank_member,
            guarantor_name=guarantor_name,
            guarantor_address=guarantor_address,
            guarantor_phone=guarantor_phone
        )
        bank_customer.save()
        return bank_customer



class Bank(models.Model):
    PERIOD_TYPES = (
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly')
    )
    STATUS_TYPES = (
        ('Open', 'open'),
        ('Progress', 'progress'),
        ('Closed', 'closed')
    )
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='member')
    name = models.CharField(unique=True, max_length=30)
    set_amount = models.FloatField()
    set_period = models.CharField(choices=PERIOD_TYPES, max_length=1)
    status = models.CharField(choices=STATUS_TYPES, default='Open', max_length=10)
    created_on = models.DateTimeField(auto_now=True)

    objects = BankManager()

    def __str__ (self):
        return self.name



class BankMembers(models.Model):
    bank_member = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='bank_member')
    bank_group = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank_group')
    guarantor_name = models.CharField(max_length=50)
    guarantor_address = models.CharField(max_length=150)
    guarantor_phone = models.CharField(max_length=20)
    guarantor_photo = models.URLField(default=getenv('PLACEHOLDER_IMAGE'))
    is_active = models.BooleanField(default=False)
    joined_on = models.DateField(auto_now=True)

    objects = BankCustomerManager()

    class Meta:
        unique_together = [['bank_member', 'bank_group']]