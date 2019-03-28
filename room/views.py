from django.shortcuts import render,reverse,redirect,HttpResponseRedirect
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render,HttpResponse,get_object_or_404
from django import views
from datetime import time
from cities_light.models import Country,Region,City
from .forms import *
from django.views import generic
from .models import *
# Create your views here.

class AddRoom(LoginRequiredMixin,views.generic.edit.FormView):
    template_name='room/add.html'
    # form_class=AddRoomForm()
    # def get_context_data(self,**kwargs):
    #     context=super(AddRoom,self).get_context_data(**kwargs)
    #     context['places']=Place.objects.filter(user=self.request.user)
    #     return context
    # form=AddRoomForm()
    # def get_form(self, form_class=None):
    #     form = super(AddRoom, self).get_form()
    #     return form

    def get_form_kwargs(self):
        kwargs=super(AddRoom,self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs

    def get_form_class(self):
        form_class_name=AddRoomForm
        return form_class_name
    
    def form_valid(self,form):
        print(form.cleaned_data.get('instrument'))
        room=form.save()
        print(room.instrument)
        for day in Day.objects.all():
            for i in range(1,24):
                slot=Slot.objects.get(pk=i)
                StaticSchedule.objects.create(room=room,slot=Slot.objects.get(pk=i),day=day)
            # slot=Slot.objects.create(i)
            # print(slot)
        return redirect('room:ManageSlots',room.id)
        # return HttpResponse('')

# class ManageSlots(LoginRequiredMixin,views.generic.edit.FormView):
#     form_class=ManageSlotsForm
#     template_name='room/ManageSlots.html'

class ManageSlots(LoginRequiredMixin,PermissionRequiredMixin,views.View):
    def has_permission(self):
            room=Room.objects.get(pk=int(self.kwargs['pk']))
            if room.place.user==self.request.user:
                return True
            return False

    def get(self,request,pk):
        context={}
        context['room']=Room.objects.get(pk=pk)
        context['slots']=StaticSchedule.objects.filter(room=context['room'])
        return render(request,'room/ManageSlots.html',context=context)

class AddPlace(LoginRequiredMixin,views.generic.edit.CreateView):
    model=Place
    form_class=AddPlaceForm
    template_name='room/addplace.html'
    def form_valid(self,form):
        print(self.request.user.id)
        form.instance.user=self.request.user
        return super(AddPlace,self).form_valid(form)
        # return HttpResponseRedirect(reverse('landing:welcome'))
    def form_invalid(self,form):
        super().form_invalid(form)
        return render(self.request,'room/addplace.html',{'form':form})
    
    def get_success_url(self):
        return reverse('landing:welcome')


def CountryLookup(request):
    cou=serializers.serialize('json',Country.objects.all())
    # print(cou)
    return JsonResponse(cou,safe=False)

def RegionLookup(request,pk):
    cou=serializers.serialize('json',Region.objects.all().filter(country_id=pk))
    return JsonResponse(cou,safe=False)

def CityLookup(request,pk):
    cou=serializers.serialize('json',City.objects.all().filter(region_id=pk))
    return JsonResponse(cou,safe=False)

def CreateSlots(request):
    for i in range(24):
        Slot.objects.create(slot=time(i))

def send_slots_by_day(request,pk):
    # schedule=StaticSchedule.objects.filter(room=Room.objects.get(pk=pk)).order_by('day')
    schedule=serializers.serialize('json',StaticSchedule.objects.filter(room=Room.objects.get(pk=pk)).order_by('day'))
    # print(schedule)
    return JsonResponse(schedule,safe=False)