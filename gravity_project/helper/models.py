import uuid

from django.core.cache import cache
from django.db import models


class CreationModificationBase(models.Model):
    """Mixin for adding creation and modification datetime."""

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="When this instance was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="When this instance was modified.")

    class Meta:
        abstract = True