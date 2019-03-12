from django.contrib import admin,sites,ModelAdmin
from booking.models import Room
from booking.forms import User


# Register your models here.

class BookingAdmin(ModelAdmin):
    form = BookingFrom

site.register(User, Room)
