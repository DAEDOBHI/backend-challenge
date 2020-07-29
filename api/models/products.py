from django.db import models


class Products(models.Model):
    product_id = models.CharField(max_length=20)
    name = models.CharField(max_length=250)
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField()
