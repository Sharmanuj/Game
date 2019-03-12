from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.

class InstrumentForm(forms.Form):
    template_name = 'instrument/instrument.html'
    form_class = UserForm

    def form_valid(self,form):
        name = form.data_get('name')