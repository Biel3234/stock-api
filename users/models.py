from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(max_length=100, null=False)

    USERNAME_FIELD = email

    def __str__(self):
        return self.name

