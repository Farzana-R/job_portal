from django import forms

from django.forms import PasswordInput, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user_app.models import UserDetails
from company_app.models import Company


class UserRegisterForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=14)
    password = forms.CharField(widget=PasswordInput())
    confirm_password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', \
            'phone_number','password', 'confirm_password']

    def save(self):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        user.save()

        phone_num = self.cleaned_data['phone_number']
        UserDetails.objects.create(user = user, 
                phone_number = phone_num,
                slug = user.username+str(user.id)).save()            
        return user


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
                raise forms.ValidationError({"password": "Password mismatch"})


    # def clean(self):
    #     # Get the user submitted names from the cleaned_data dictionary
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get("username")
    #     first_name = cleaned_data.get("first_name")
    #     last_name = cleaned_data.get("last_name")
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password != confirm_password:
    #         print('password mismatch error')
    #         # If not, raise an error
    #         raise forms.ValidationError("The username must contains at least 4 letters")

    #     # Check if the first letter of both names is the same
    #     if len(username) < 4:
    #         print(len(username))
    #         # If not, raise an error
    #         raise ValidationError("both passwords are not matching")

    #     return cleaned_data


class CompanyRegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=101)
    # email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = forms.CharField(max_length=14)
    password = forms.CharField(widget=PasswordInput())
    confirm_password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'name', 'email', \
            'phone_number','password', 'confirm_password']

    def save(self):
        
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        user.save()

        phone_num = self.cleaned_data['phone_number']
        name = self.cleaned_data['name']
        Company.objects.create(name = name,
        user = user,
        phone_number = phone_num,
        slug = user.username+str(user.id)).save()               
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
