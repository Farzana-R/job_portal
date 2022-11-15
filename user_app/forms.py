from django import forms
from django.forms import CharField, PasswordInput
from django.contrib.auth.models import User
from .models import UserDetails


class uf(forms.ModelForm):
    password = CharField(widget=PasswordInput())
    confirm_password = CharField(widget=PasswordInput())
    class Meta:
        model = User 
        fields = ['username', 'email', 'password', 'confirm_password']
        

    def save(self):
        user = super().save(commit=False)
        user.save()

        UserDetails.objects.create(user = user,  
                phone_number = '1234', slug = 's'+str(user.id)).save()

        return user   

class UserForm(forms.Form):
    username = forms.CharField(help_text = "username")
    first_name = forms.CharField(help_text = "first_name") 
    last_name = forms.CharField(help_text = "last_name") 
    email = forms.CharField(help_text = "email")
    
    password = forms.CharField(help_text = "password")
    confirm_password = forms.CharField(help_text = "confirm_password")

    def save(self):
        user = super().save(commit=False)
        print('override save...')
        # user.is_student = True
        # user.save()
        # student = Student.objects.create(user=user)
        # student.interests.add(*self.cleaned_data.get('interests'))
        return user
    
    
class CompanyForm(forms.Form):
    username = forms.CharField(help_text = "username")
    email = forms.CharField(help_text = "email")    
    password = forms.CharField(help_text = "password")
    confirm_password = forms.CharField(help_text = "confirm_password")
    