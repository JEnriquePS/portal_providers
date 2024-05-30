import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CustomUser(AbstractBaseModel, AbstractUser):
    ROLE_CHOICES = (
        ('CO', 'Colocador de solicitudes'),
        ('AP', 'Aprobador de solicitudes'),
    )

    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='CO')