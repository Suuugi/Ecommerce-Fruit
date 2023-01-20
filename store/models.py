from django.db import models

class Product(models.Model):
    """A model of a product being sold in a store"""
    name = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0.00)
    image = models.CharField(max_length=200, default="")

    class Meta:
        ordering = ['name']