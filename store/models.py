from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """A model of a product being sold in a store"""
    name = models.CharField(max_length=50, default="")
    price = models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=200, default="")

    class Meta:
        ordering = ['name']


class Catalog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=10)
    selling_product = models.BooleanField(default=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
