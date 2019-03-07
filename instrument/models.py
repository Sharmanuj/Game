from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Room(models.Model):
    room_name = models.CharField(max_length=100)
    instrument = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.room_name

    class Meta:
        ordering = ('room_name',)
