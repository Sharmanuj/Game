from django.db import models
from room.models import Room
from accounts.models import User

# Create your models here.

class Booking(models.Model):
    room = models.ManyToManyField(Room)
    user = models.ManyToManyField(User)
    slot = models.TimeField('Show Start Time', )
    # duration = models.DurationField('Duration',)
    # slot_end_time = models.TimeField('Show End Time (Optional)',blank=True, null=True )
    confirm = models.BooleanField(defaul=True)