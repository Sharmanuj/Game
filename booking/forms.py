from django import forms
from instrument.forms import Instrument
from room.models import Place
# from user.forms import User

class SearchRoomForm(forms.ModelForm):
    date=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Place
        fields=['country','region','city']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["date"].widget.attrs.update({"class":"browser-default custom-select"})

# class BookingFrom(forms.ModelForm):
#     instrument = forms.MultipleChoiceField()
#     class Meta:
#         model = Instrument

#     user = forms.MultipleChoiceField()
#     slot = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
#     confirm = forms.BooleanField(required=False,initial=False,label='Extra cheeze')


    


                                      