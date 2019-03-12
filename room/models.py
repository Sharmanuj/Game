from django.db import models
from instrument.models import Instrument
from address.models import AddressField
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
