from tkinter import CASCADE
from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="Best service")


class OsPlatform(models.Model):
    LINUX = "LN"
    WINDOWS = "WD"
    OS_TYPE_CHOICES = [
        (LINUX, "Linux"),
        (WINDOWS, "Windows"),
    ]

    type = models.CharField(max_length=2,
                            choices=OS_TYPE_CHOICES)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="Easy to setup")


class ServicePrice(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    os = models.ForeignKey(OsPlatform, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)