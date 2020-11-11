from django.db import models


# Creating model CurrencyRate with two fields
class CurrencyRate(models.Model):
    uah_rate = models.FloatField(blank=False)
    date = models.DateField(blank=False)
