from django import forms



class UserForm(forms.Form):
    Name = forms.CharField(label='name', max_length=100)