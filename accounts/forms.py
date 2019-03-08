from django import forms
from address.forms import AddressField
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from address.forms import AddressField
from creditcards.forms import CardNumberField
from .models import Host
class BecomeHostForm(forms.ModelForm):
    cc_no=CardNumberField(label='credit card number')
    class Meta:
        model=Host
        fields=('address','country')
        widgets={'country':CountrySelectWidget()}
