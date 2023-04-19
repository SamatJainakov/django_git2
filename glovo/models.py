from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    amount = models.IntegerField()
    courier = models.ForeignKey('Courier', on_delete=models.CASCADE)
