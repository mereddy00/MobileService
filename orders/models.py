from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

user_type = [
    ("Staff", "Staff"),
    ("Customer", "Customer")
]


class OrderStatus(models.Model):
    status = models.CharField(max_length=255)


class Order(models.Model):

    employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="employee")
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="customer")
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    mobile_brand = models.CharField(max_length=255)
    mobile_model = models.CharField(max_length=255)
    mobile_IMEI = models.CharField(max_length=255)
    estimated_amount = models.IntegerField()
    estimated_date = models.DateField()


