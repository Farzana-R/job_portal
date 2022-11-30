from django.contrib import messages, auth
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View

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
        request, 'admin_app/login.html',\
             context={'form': form, 'message': message})


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