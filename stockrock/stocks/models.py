from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
