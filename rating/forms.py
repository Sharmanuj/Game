from django import forms
from models.django import RatingStar


class RatingName(forms.Form):
    class Meta:
        model = RatingStar
        fields = ('rating')