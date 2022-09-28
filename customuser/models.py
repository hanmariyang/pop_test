from ctypes import addressof
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomModel(AbstractUser):

    class Meta:
        db_table = 'custom_user'
    
    address = models.TextField(max_length=500, blank=True)
    bio = models.TextField(max_length=500, blank=True)