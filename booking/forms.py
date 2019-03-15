from django import forms
from instrument.forms import Instrument
# from user.forms import User



class BookingFrom(forms.ModelForm):
    instrument = forms.MultipleChoiceField()
    class Meta:
        model = Instrument

    user = forms.MultipleChoiceField()
    slot = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    confirm = forms.BooleanField(required=False,initial=False,label='Extra cheeze')


    


                                      