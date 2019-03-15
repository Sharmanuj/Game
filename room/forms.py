from django import forms
from .models import *
# from instrument.forms import Instrument
from address.forms import AddressField
from instrument.models import Instrument

class AddRoomForm(forms.ModelForm):
    # capacity = forms.CharField(max_length=100)
    # size = forms.CharField(max_length=100)
    # address = AddressField()
    # place = forms.MultipleChoiceField(choices=Place.objects.filter(user=1))
    # postal_code = forms.CharField(max_length=100)
    # instrument = forms.MultipleChoiceField(choices=Instrument.objects.all())
    class Meta:
        model=Room
        fields=['name','place','size','capacity','instrument']
        widgets = {
            'instrument':  forms.CheckboxSelectMultiple()
        } 
    def __init__(self, **kwargs):
        user=kwargs.pop('user')
        super(AddRoomForm, self).__init__(**kwargs)
        print(self)
        self.fields['place'].queryset=Place.objects.filter(user=user)

class AddPlaceForm(forms.ModelForm):
    class Meta:
        model=Place
        fields=['address','country','region','city']
