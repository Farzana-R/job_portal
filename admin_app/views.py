from django.conf import settings
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import View

from company_app.models import Job

from . import forms


class Home(View):
    def get(self, request):
        jobs = Job.objects.all()[:3]
        return render(request, 'index.html', {'jobs' : jobs})


class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        context={'form': form}
        return render(request, 'admin_app/login.html', context)
    
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
        return render(request, 'admin_app/login.html', context)





class About(View):
    def get(self, request):
        return render(request, 'design/about.html')


class Contact(View):
    def get(self, request):
        return render(request, 'design/contact.html')



class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('home')
