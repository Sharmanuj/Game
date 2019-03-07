from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from address.models import AddressField
# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username
    email=models.EmailField(unique=True)
    phone_number=PhoneNumberField(unique=True,max_length=15,blank=True,null=True)
    is_host=models.BooleanField(default=False)
    REQUIRED_FIELDS=['email']


class Host(models.Model):
    # address=models.CharField(max_length=1024)
    verified_to_host=models.BooleanField(default=False)
    country=CountryField()
    address=AddressField(on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)