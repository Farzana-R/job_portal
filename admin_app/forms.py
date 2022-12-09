from django import forms
from django.forms import PasswordInput
from django.contrib.auth.models import User

from user_app.models import UserDetails
from company_app.models import Company


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
