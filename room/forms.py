from django import forms
from .models import Place
from instrument.forms import Instrument
from address.forms import AddressField


class UserForm(forms.Form):
    capacity = forms.CharField(max_length=100)
    size = forms.CharField(max_length=100)
    address = AddressField(max_length=300)
    # place = forms.ForeignKey(Place)
    postal_code = forms.CharField(max_length=100)
    instrument = forms.MultipleChoiceField(Instrument.objects.all())

class AddPlaceForm(forms.ModelForm):
    class Meta:
        model=Place
        fields=['address','country','region','city']
