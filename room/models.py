from django.db import models

# Create your models here.
class Room(models.Model):
    capacity = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    # time = models.TimeField()