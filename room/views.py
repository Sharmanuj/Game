from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *

# Create your views here.

class CustomerFormView(generic.edit.FormView):
    template_name='room/room.html'
    form_class=UserForm
    # success_url='//'
    
    def form_valid(self,form):
        msg=""
        capacity=form.data.get("capacity")
        size=form.data.get("size")
        address = form.data.get("address")
        postal_code = form.data.get("postal_code")
    
    