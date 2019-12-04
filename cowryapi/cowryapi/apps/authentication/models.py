from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token

from os import getenv

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        email = kwargs.get(
            'email')
        first_name = kwargs.get(
            'first_name')
        last_name = kwargs.get(
            'last_name')
        telephone = kwargs.get(
            'telephone')
        password = kwargs.get(
            'password')
        user = self.model(email=email,
                        first_name=first_name,
                        last_name=last_name,
                        telephone=telephone,
                        password=password)
        user.set_password(
            password)
        user.is_superuser = False
        user.save()
        Token.objects.create(user=user)
        return user

    def create_superuser(self, **kwargs):
        email = kwargs.get('email')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        telephone = kwargs.get('telephone')
        password = kwargs.get('password')
        user = self.model(email=email,
                          first_name=first_name,
                          last_name=last_name,
                          telephone=telephone,
                          password=password)
        user.set_password(password)
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    profile_image = models.URLField(default=getenv('PLACEHOLDER_IMAGE'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name (self):
        return (f"{self.first_name} {self.last_name}")
    
    def short_name (self):
        return self.first_name

    def __str__ (self):
        return self.email

