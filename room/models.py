from django.db import models
from cities_light.models import Country
from accounts.models import User
# from cities_light.forms import Country
# Create your models here.
# class City(models.Model):
class Place(models.Model):
    address=models.CharField(max_length=1024)
    city=models.ForeignKey('cities_light.City',on_delete=models.CASCADE)
    region=models.ForeignKey('cities_light.region',on_delete=models.CASCADE)
    country=models.ForeignKey('cities_light.Country',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Timing(models.Model):
    slot=models.TimeField()
    price=models.DecimalField(max_digits=3,decimal_places=2)