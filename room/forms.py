from django import forms
from .models import Place
class AddPlaceForm(forms.ModelForm):
    class Meta:
        model=Place
        fields=['address','country','region','city']