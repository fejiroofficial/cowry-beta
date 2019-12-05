from django.db import models
from cowryapi.apps.authentication.models import CustomUser

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

