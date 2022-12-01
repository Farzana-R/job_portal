from django.contrib import messages, auth
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.views.generic import View

from . import forms

# Create your views here.


class CompanyRegister(View):

    def get(self, request):
        company_form = forms.CompanyRegisterForm()
        context = {'form': company_form}
        return render(request, 'company_app/register.html', context)

    def post(self, request):
        company_form = forms.CompanyRegisterForm(request.POST) 
        if company_form.is_valid():
            company_form.save()
            return redirect('loginview')
        context = {'form': company_form}
        return render(request, 'company_app/register.html', context)


class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        context={'form': form}
        return render(request, 'company_app/login.html', context)
    
    def post(self, request):
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
        return render(request, 'company_app/login.html', context)