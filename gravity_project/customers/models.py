from django.db import models
from helper.models import CreationModificationBase
from helper import regex_validators


# Create your models here.

class Customer(CreationModificationBase):
    """Model to store customers data"""

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(validators = [regex_validators.phone_regex], max_length = 10)
    address = models.TextField()