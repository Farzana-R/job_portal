from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from . models import UserDetails


class UserUpdateProfileForm(forms.ModelForm):   
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    class Meta:
        model = UserDetails
        fields = ['first_name','address', 'date_of_birth', 'phone_number', 'image',\
            'description']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
