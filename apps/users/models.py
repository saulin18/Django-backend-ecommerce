from django.db import models
from .managers import CustomUserManager
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    bio = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(default='user.png')
    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return f'{self.username}'