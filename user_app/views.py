from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from .models import UserDetails


class UserRegistration(View):
    def get(self, request):
        return render(request, 'user_app/registration.html')

    def post(self, request):
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        # Backend Validation

        #Dictionary to temporarly store entered values
        data = {
            'username' : username,
            'firstname' : firstname,
            'lastname' : lastname,
            'email' : email,
            'phone' : phone,  
            'password' : password, 
            'confirmpassword' : confirmpassword,        
        }

        user = User.objects.create(username = username,
                first_name = firstname, last_name = lastname,
                email = email)
        user.set_password(password)
        user.save()

        UserDetails.objects.create(user = user,  
                phone_number = phone).save()

        return render(request, 'user_app/registration.html', data)


class UserLogin(View):
    def get(self, request):
        return render(request, 'user_app/login.html')

    def post(self, request):
        pass