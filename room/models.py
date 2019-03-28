from django.db import models
from instrument.models import Instrument
from address.models import AddressField
from cities_light.models import Country
from accounts.models import User
from djmoney.models.fields import MoneyField
# from place.models import Place
# Create your models here.

    
class Place(models.Model):
    def __str__(self):
        # return "{}_{}".format(self.user.username,self.address)
        return "{}".format(self.address)
    address=models.CharField(max_length=1024)
    city=models.ForeignKey('cities_light.City',on_delete=models.CASCADE)
    region=models.ForeignKey('cities_light.region',on_delete=models.CASCADE)
    country=models.ForeignKey('cities_light.Country',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Room(models.Model):
    name=models.CharField(max_length=20,unique=True)
    capacity = models.PositiveIntegerField()
    size = models.DecimalField(max_digits=7,decimal_places=2)
    # address = AddressField(on_delete=models.CASCADE)
    # place = models.ForeignKey(Place)
    postal_code = models.CharField(max_length=100)
    instrument = models.ManyToManyField(Instrument)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        app_label = 'room'

class Day(models.Model):
    def __str__(self):
        return self.day
    day=models.CharField(max_length=10)


class Slot(models.Model):
    def __str__(self):
        return "{}".format(self.slot)
    slot=models.TimeField()
    # price = MoneyField(
    #     decimal_places=2,
    #     default=0,
    #     default_currency='USD',
    #     max_digits=11,
    # )
    # room=models.ForeignKey(Room,on_delete=models.CASCADE)

class StaticSchedule(models.Model):
    def __str__(self):
        return "{}_{}".format(self.room,self.slot)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    slot=models.ForeignKey(Slot,on_delete=models.CASCADE)
    day=models.ForeignKey(Day,on_delete=models.CASCADE)
    # is_active=models.BooleanField(default=False)
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )