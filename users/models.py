from django.contrib.auth.models import AbstractUser
from django.db import models

user_type = [
    ("Staff", "Staff"),
    ("Customer", "Customer")
]


class CustomUser(AbstractUser):
    address = models.CharField(max_length=50, default=' ', null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=user_type, null=True, blank=True)