from django.contrib import messages, auth
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.views.generic import View

from . import forms


class Home(View):
    def get(self, request):
        return render(request, 'index.html')


class About(View):
    def get(self, request):
        return render(request, 'design/about.html')


class Contact(View):
    def get(self, request):
        return render(request, 'design/contact.html')


class UserRegister(View):

    def get(self, request):
        user_form = forms.UserRegisterForm()
        context = {'form': user_form}
        return render(request, 'admin_app/register.html', context)

    def post(self, request):
        user_form = forms.UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            #Send mail
            email=user_form.cleaned_data['email']
             
            send_mail('HI WELCOME ...',
                'Hi welcome to JOBRIAL',
                settings.EMAIL_HOST_USER,[email],fail_silently=False)
            return redirect('loginview')
        messages.error(request,'password not matching')
        context = {'form': user_form}
        return render(request, 'admin_app/register.html', context)


class CompanyRegister(View):

    def get(self, request):
        company_form = forms.CompanyRegisterForm()
        context = {'form': company_form}
        return render(request, 'admin_app/register.html', context)

    def post(self, request):
        
        company_form = forms.CompanyRegisterForm(request.POST)
        
        
        
        # confirmpassword = request.POST['confirmpassword']
        if company_form.is_valid():
            company_form.save()
            return redirect('loginview')
        context = {'form': company_form}
        return render(request, 'admin_app/register.html', context)


def loginview(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Login failed!'
    return render(
        request, 'admin_app/login.html', context={'form': form, 'message': message})


def logout(request):
    auth.logout(request)
    return redirect('home')

# this function not used yet
def change_password(request):
    u = User.objects.get(username='john')
    u.set_password('new password')
    u.save()


# def home(request):
#     return render(request, 'index.html')