from django import forms
from instrument.models import Instrument



class UserForm(forms.Form):
    Name = forms.CharField(label='name', max_length=100)