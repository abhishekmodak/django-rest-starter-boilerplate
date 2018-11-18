from django.db import models
from django.contrib.auth.models import AbstractUser
from factory.models import BaseModel

# Create your models here.


class User(AbstractUser, BaseModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.CharField(max_length=64, unique=True)
