from django.db import models

from applications.custom_users.models import CustomUser, AbstractBaseModel


class Order(AbstractBaseModel):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    request_placer = models.ForeignKey(CustomUser, related_name='placed_orders', on_delete=models.CASCADE, limit_choices_to={'role': 'CO'})
    request_approver = models.ForeignKey(CustomUser, related_name='approved_orders', on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'AP'})
    approved = models.BooleanField(default=False)
