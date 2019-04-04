from django.contrib import admin,sites
from booking.models import Room
from .models import *
# from booking.forms import User


# Register your models here.

# class BookingAdmin(ModelAdmin):
#     form = BookingFrom

admin.site.register(Room_Reservations)
admin.site.register(Booking)
