from django.db import models
from django.contrib.auth.models import AbstractUser


class FullName(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Address(models.Model):
    no_house = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class User(AbstractUser):
    fullname = models.OneToOneField(FullName, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
