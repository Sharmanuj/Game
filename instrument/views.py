from django.shortcuts import render
from .models import *
from .forms import *
from django import views

# Create your views here.

class InstrumentForm(views.generic.edit.FormView):
    template_name = 'instrument/instrument.html'
    form_class = UserForm

    def form_valid(self,form):
        name = form.data_get('name')