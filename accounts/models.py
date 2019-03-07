from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username
    email=models.EmailField(unique=True)
    phone_number=PhoneNumberField(unique=True,max_length=15,blank=True,null=True)
    REQUIRED_FIELDS=['email']