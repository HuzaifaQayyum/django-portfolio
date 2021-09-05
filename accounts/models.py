from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email           = models.EmailField(unique=True)
    password        = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    name            = models.CharField(max_length=100)

    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']