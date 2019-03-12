from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from address.models import AddressField
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username
    email=models.EmailField(unique=True)
    phone_number=PhoneNumberField(unique=True,max_length=15,blank=True,null=True)
    applied_to_host=models.BooleanField(default=False)
    is_host=models.BooleanField(default=False)
    REQUIRED_FIELDS=['email']


class Host(models.Model):
    def __str__(self):
        return self.user.username
    # address=models.CharField(max_length=1024)
    verified_to_host=models.BooleanField(default=False)
    country=CountryField()
    # cc_no=models.ForeignKey(CreditCardNumber,on_delete=models.CASCADE)
    address=AddressField(on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class CreditCardNumber(models.Model):
    def __str__(self):
        return "{}_{}".format(self.user.username,self.cc_no)
    cc_no=CardNumberField(_('card number'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)