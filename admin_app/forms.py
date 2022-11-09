from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SelectForm(forms.Form):
    CHOICES = [('user', 'user',), ('company', 'company',)]
    select = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = User
        fields = ['select']


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = forms.CharField(max_length=14)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', \
            'phone_number','password1', 'password2'] 

class CompanyRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=101)
    email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = forms.CharField(max_length=14)

    class Meta:
        model = User
        fields = ['username', 'name', 'email', \
            'phone_number','password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)