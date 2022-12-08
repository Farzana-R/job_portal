from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from . import forms
from company_app.models import Company


class Home(View):
    def get(self, request):
        # jobs = Job.objects.all()[:3]
        return render(request, 'company_app/company_home.html')


# view company profile
@method_decorator(login_required, name='get')
class CompanyProfile(View):
    def get(self, request):
        company_details = Company.objects.get(user=request.user)
        return render(request, 'company_app/dashboard.html', {'company_details': company_details})


# edit company profile
@method_decorator(login_required, name='get')
class UpdateCompanyProfile(View):
    def get(self, request):
        form = forms.CompanyUpdateProfileForm()
        return render(request, 'company_app/edit_profile.html', {'form': form})

    def post(self, request):
        profile = Company.objects.filter(user=request.user).first()
        form = forms.CompanyUpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('company_app:company_profile')
        else:
            return render(request, 'company_app/edit_profile.html', {'form': form})


class CompanyRegister(View):

    def get(self, request):
        company_form = forms.CompanyRegisterForm()
        context = {'form': company_form}
        return render(request, 'company_app/register.html', context)

    def post(self, request):
        company_form = forms.CompanyRegisterForm(request.POST) 
        if company_form.is_valid():
            company_form.save()
            return redirect('company_app:login')
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
                return redirect('company_app:company_home')
        return render(request, 'company_app/login.html', context)