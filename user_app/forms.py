from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User

from . models import UserDetails

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        # def get_object(self):
        #     return self.request.user

        

    



class UserUpdateProfileForm(forms.ModelForm):   
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'})) 
    class Meta:
        model = UserDetails
        fields = ['address', 'location', 'country', 'date_of_birth', \
            'phone_number', 'image', 'description', 'resume',\
                'grad_year', 'looking_for']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=14)
    password = forms.CharField(widget=PasswordInput())
    confirm_password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', \
            'phone_number','password', 'confirm_password']    

    def clean(self):
        super(UserRegisterForm, self).clean()

        username = self.cleaned_data.get('username') 
        first_name = self.cleaned_data.get('first_name') 
        last_name = self.cleaned_data.get('last_name') 
        phone_number = self.cleaned_data.get('phone_number') 
        password= self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
          
        if len(username) < 4 :
            raise forms.ValidationError({"username":"Username \
                                        should be atleat \
                                        4 character long."})
        
        if not first_name.isalpha():
            raise forms.ValidationError({"first_name":"First name \
                                        should not containe \
                                        any digits or \
                                        special characters."})
       
        if not last_name.isalpha():
            raise forms.ValidationError({"last_name":"Last name \
                                        should not containe \
                                        any digits or \
                                        special characters."})

        if not phone_number.isdigit():
            raise forms.ValidationError({"phone_number":"Invalid \
                                        phone number."})

        if password != confirm_password:
            raise forms.ValidationError({"password": "Password \
                                        mismatch"})

    def save(self):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        user.save()

        phone_num = self.cleaned_data['phone_number']
        UserDetails.objects.create(user = user, phone_number = phone_num,
                slug = user.username+str(user.id)).save()            
        return user