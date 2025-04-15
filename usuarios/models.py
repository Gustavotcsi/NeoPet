from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class Users(AbstractUser):
    choices_cargo = (('V', 'Vendedor'), ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choices_cargo)

    groups = models.ManyToManyField(Group, related_name='usuarios_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_users', blank=True)
