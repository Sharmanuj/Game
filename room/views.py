from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render,HttpResponse,get_object_or_404
from django import views
from cities_light.models import Country,Region,City
from .forms import *
# Create your views here.
class AddRoom(views.View):
    def get(self,request):
        return render(request,'room/add.html')

class AddPlace(views.generic.edit.FormView):
    form_class=AddPlaceForm

# def add(request):
    # return render(request,'room/add.html')

def CountryLookup(request):
    cou=serializers.serialize('json',Country.objects.all())
    return JsonResponse(cou,safe=False)

def RegionLookup(request,pk):
    cou=serializers.serialize('json',Region.objects.all().filter(country_id=pk))
    return JsonResponse(cou,safe=False)

def CityLookup(request,pk):
    cou=serializers.serialize('json',City.objects.all().filter(region_id=pk))
    return JsonResponse(cou,safe=False)