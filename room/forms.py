from django import forms
from .models import Place
from instrument.forms import Instrument
from address.forms import AddressField


class UserForm(forms.Form):
    capacity = forms.CharField(max_length=100)
    size = forms.CharField()
    address = AddressField()
    # place = forms.ForeignKey(Place)
    postal_code = forms.CharField(max_length=100)
    instrument = forms.MultipleChoiceField()

class AddPlaceForm(forms.ModelForm):
    class Meta:
        model=Place
        fields=['address','country','region','city']
