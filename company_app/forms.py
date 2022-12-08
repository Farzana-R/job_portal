from django import forms

from django.forms import PasswordInput, ValidationError
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from company_app.models import Company


class CompanyUpdateProfileForm(forms.ModelForm):    

    class Meta:
        model = Company
        fields = ['name','address', 'phone_number', 'logo',\
            'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


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

    def clean(self):
            super(CompanyRegisterForm, self).clean()
       
            username = self.cleaned_data.get('username') 
            name = self.cleaned_data.get('name') 
            phone_number = self.cleaned_data.get('phone_number') 
            password= self.cleaned_data.get('password')
            confirm_password = self.cleaned_data.get('confirm_password')
          
            if len(username) < 4 :
                raise forms.ValidationError({"username":"Username \
                                            should be atleat \
                                            4 character long."})

            if len(name) < 3 :
                raise forms.ValidationError({"username":"Username \
                                            should be atleat \
                                            4 character long."})
        

            if not phone_number.isdigit():
                raise forms.ValidationError({"phone_number":"Invalid \
                                            phone number."})

            if password != confirm_password:
                raise forms.ValidationError({"password": "Password mismatch"})


