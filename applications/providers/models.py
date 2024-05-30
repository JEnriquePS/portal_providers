from django.db import models

from applications.custom_users.models import AbstractBaseModel, CustomUser


class Provider(AbstractBaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Partnership(AbstractBaseModel):
    request_placer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
