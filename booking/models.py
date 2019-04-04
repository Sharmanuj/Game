from django.db import models
from djmoney.models.fields import MoneyField
from room.models import Room,StaticSchedule
from accounts.models import User
# Create your models here.

class Booking(models.Model):
    room = models.ManyToManyField(Room)
    user = models.ManyToManyField(User)
    amount=MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )
    order_date=models.DateTimeField(auto_now=True)
    # duration = models.DurationField('Duration',)
    # slot_end_time = models.TimeField('Show End Time (Optional)',blank=True, null=True )
    options=[
        ('confirmed','confirm'),
        ('waiting','Waiting'),
        ('canceled','Cancel')
    ]
    status=models.CharField(
        choices=options,
        default='waiting',
        max_length=10
    )

class Room_Reservations(models.Model):
    slot=models.ForeignKey(StaticSchedule,on_delete=models.CASCADE)
    date=models.DateField()
    order=models.ForeignKey(Booking,on_delete=models.CASCADE)