from django import forms

from django.forms import PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user_app.models import UserDetails
from company_app.models import Company


class UserRegisterForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=14)
    password = forms.CharField(widget=PasswordInput())
    password2 = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', \
            'phone_number','password', 'password2']

    def save(self):
        print('check 3')
        user = super().save(commit=False)
        user.save()
        UserDetails.objects.create(user = user,  
                phone_number = '123', slug = 's'+str(user.id)).save()               
        return user


class CompanyRegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=101)
    # email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = forms.CharField(max_length=14)
    password = forms.CharField(widget=PasswordInput())
    password2 = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'name', 'email', \
            'phone_number','password', 'password2']

    def save(self):
        print('check 3')
        user = super().save(commit=False)
        user.save()
        Company.objects.create(name = 'name' ,user = user,  
                phone_number = '123', slug = 's'+str(user.id)).save()               
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)










    # class UserRegisterForm(UserCreationForm):
#     first_name = forms.CharField(max_length=101)
#     last_name = forms.CharField(max_length=101)
#     email = forms.EmailField(max_length=200, help_text='Required')
#     phone_number = forms.CharField(max_length=14)

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', \
#             'phone_number','password1', 'password2']

#     def save(self):
#         print('check 3')
#         user = super().save(commit=False)
#         user.save()
#         UserDetails.objects.create(user = user,  
#                 phone_number = '123', slug = 's'+str(user.id)).save()               
#         return user
