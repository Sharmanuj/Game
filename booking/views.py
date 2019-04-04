from django.shortcuts import render,reverse,HttpResponseRedirect
from django.urls import reverse_lazy
from cities_light.models import City
from django import views
from room.models import Room
from .forms import *
# Create your views here.

class SearchRoom(views.generic.edit.FormView):
    form_class=SearchRoomForm
    template_name='booking/search.html'
    def get_success_url(self):
        city=City.objects.get(display_name=self.form.cleaned_data['city'])
        print(city.id)
        return reverse_lazy('booking:list-room',args=[city.id])
    
    def form_valid(self,form):
        self.form=form
        return HttpResponseRedirect(self.get_success_url())

class ListRoom(views.generic.ListView):
    template_name='booking/RoomList.html'
    model=Room
    def get_queryset(self):
        return Room.objects.filter(place__city=self.kwargs["city"])