from django.db import models

from applications.custom_users.models import AbstractBaseModel
from applications.orders.models import Order
from applications.providers.models import Provider


class Product(AbstractBaseModel):
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    link = models.URLField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

