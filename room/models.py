from django.db import models
from instrument.models import Instrument
from address.models import AddressField
from cities_light.models import Country
from accounts.models import User
# from place.models import Place
# Create your models here.


class Room(models.Model):
    capacity = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    address = AddressField(on_delete=models.CASCADE)
    # place = models.ForeignKey(Place)
    postal_code = models.CharField(max_length=100)
    instrument = models.ManyToManyField(Instrument)

    # def __str__(self):
    #     return self.name

    class Meta:
        app_label = 'room'
  
  
  class Place(models.Model):
    address=models.CharField(max_length=1024)
    city=models.ForeignKey('cities_light.City',on_delete=models.CASCADE)
    region=models.ForeignKey('cities_light.region',on_delete=models.CASCADE)
    country=models.ForeignKey('cities_light.Country',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
