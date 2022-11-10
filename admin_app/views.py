
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

from . import forms

class Home(View):
    def get(self, request):
        return render(request, 'index.html')


# def home(request):
#     return render(request, 'index.html')


def user_register(request):

    if request.method == 'POST':
        
        user_form = forms.UserRegisterForm(request.POST)
        print("check 1")
        if user_form.is_valid():
            print('check 2')
            # user = user_form.save(commit=False)
            # user.save()
            # user = authenticate(request, username=user.username, \
            #     password=request.POST['password1'])
            user_form.save()
            return redirect('login')
    else:
        user_form = forms.UserRegisterForm()
    context = {'form': user_form}
    return render(request, 'admin_app/register.html', context)


def company_register(request):

    if request.method == 'POST':
        company_form = forms.CompanyRegisterForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return redirect('login')
    else:
        company_form = forms.CompanyRegisterForm()


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