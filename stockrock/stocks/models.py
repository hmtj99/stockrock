from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length = 100)
    ticker = models.CharField(max_length = 100)

    def __str__(self):
        return self.name