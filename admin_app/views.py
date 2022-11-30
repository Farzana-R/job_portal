from django.contrib import messages, auth
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.views.generic import View

from company_app.models import Job

from . import forms


class Home(View):
    def get(self, request):
        jobs = Job.objects.all()[:3]
        return render(request, 'index.html', {'jobs' : jobs})


class About(View):
    def get(self, request):
        return render(request, 'design/about.html')


class Contact(View):
    def get(self, request):
        return render(request, 'design/contact.html')


class UserRegister(View):
    def get(self, request):
        user_form = forms.UserRegisterForm()
        context = {'form' : user_form}
        return render(request, 'admin_app/register.html', context)

    def post(self, request):
        user_form = forms.UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            # Sending  mail to registered user
            email=user_form.cleaned_data['email']             
            send_mail('HI WELCOME ...',
                'Hi welcome to JOBRIAL',
                settings.EMAIL_HOST_USER, [email], fail_silently=False)
            return redirect('loginview')

        context = {'form' : user_form}
        return render(request, 'admin_app/register.html', context)



class CompanyRegister(View):
    def get(self, request):
        company_form = forms.CompanyRegisterForm()
        context = {'form': company_form}
        return render(request, 'admin_app/register.html', context)

    def post(self, request):
        company_form = forms.CompanyRegisterForm(request.POST)
            
        if company_form.is_valid():
            company_form.save()
            return redirect('loginview')

        context = {'form': company_form}
        return render(request, 'admin_app/register.html', context)


class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        context={'form': form}
        return render(request, 'admin_app/login.html', context)
    
    def post(self, request):
def loginview(request):
    form = forms.LoginForm()
    message = ''

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        context={'form': form}

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'admin_app/login.html', context)

            else:
                message = 'Login failed!'

    return render(
        request, 'admin_app/login.html',\
             context={'form': form, 'message': message})


class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('home')
