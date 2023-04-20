from django.db import models


class Courier(models.Model):
    full_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
