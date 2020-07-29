from django.db import models


class Products(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=250)
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField()
