from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views import View

# class based view for registration
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password1']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Taken')
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Taken')
                return redirect('register.html')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                # send_mail('Registration successful','Login to see more!!',settings.EMAIL_HOST_USER,[username])
                return redirect('login.html')
        else:
            messages.info(request, 'password not matching...')
            return redirect('register.html')


# class based view for login page
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('home_page.html')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login.html')

# logout
def logout(request):
    auth.logout(request)
    return redirect('/')