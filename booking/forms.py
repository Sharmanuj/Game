from django import forms
from instrument.forms import Instrument
from user.forms import User



class BookingFrom(forms.ModelForm):
    class Meta:
        modal = Instrument
        exclude = 
    instrument = forms.MultipleChoiceField(Instrument.objects.all())
    class Meta:
        model = Instrument

    user = forms.MultipleChoiceField(User.objects.all())
    slot = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    confirm = forms.BooleanField(required=False,initial=False,label='Extra cheeze')


    


                                      