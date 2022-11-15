from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from .models import UserDetails
from .forms import UserForm, CompanyForm, uf


class UserRegistration(View):
    def get(self, request):
        context ={}
        context['user_form']= UserForm()
        context['company_form']= CompanyForm()
        context['uf']= uf()
        return render(request, 'user_app/registration.html', context)

    def post(self, request):
        form = uf(request.POST or None, request.FILES or None)
     
        # check if form data is valid
        if form.is_valid():
            print('valid')
            user = form.save()
            # Cleaned(normalized) data
            
            password = form.cleaned_data['password']
            print(password)

            #  Use set_password here
            user.set_password(password)
            user.save()
            #form.save()
         
        
            
            
        # user_form = UserForm(request.POST, None)  
        # company_form = CompanyForm(request.POST, None)

        # if user_form.is_valid():  
        #     print('user form', user_form)
        #     print('user')
        
        # if company_form.is_valid(): 
        #     print('company form', company_form) 
        #     print('company')
        # username = request.POST['username']
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        # email = request.POST['email']
        # phone = request.POST['phone']
        # password = request.POST['password']
        # confirmpassword = request.POST['confirmpassword']

        # #Backend Validation

        # #Dictionary to temporarly store entered values
        # data = {
        #     'username' : username,
        #     'firstname' : firstname,
        #     'lastname' : lastname,
        #     'email' : email,
        #     'phone' : phone,  
        #     'password' : password, 
        #     'confirmpassword' : confirmpassword,        
        # }

        # user = User.objects.create(username = username,
        #         first_name = firstname, last_name = lastname,
        #         email = email)
        # user.set_password(password)
        # user.save()

        # UserDetails.objects.create(user = user,  
        #         phone_number = phone, slug = 's'+str(user.id)).save()

        return render(request, 'user_app/registration.html')


import requests
class UserLogin(View):
    def get(self, request):           
        # url = "https://www.fast2sms.com/dev/bulkV2"
  
        # querystring = {
        #     "authorization": "VEgXoe7WSDsA8BUIw3MChyTQbLKjZ6HnNkarY2i5vRpqGtz0OchBPMN1rxz7GokXIVmjb38EYvJ0ClTi",
        #     "message": "This is test Message sent from \
        #     Python Script using REST API.",
        #     "language": "english",
        #     "route": "q",
        #     "numbers": "7356627414, 8590017269"
        # }
  
        # headers = {
        #     'cache-control': "no-cache"
        # }
        # try:
        #     response = requests.request("GET", url,
        #                         headers = headers,
        #                         params = querystring)
      
        #     print("SMS Successfully Sent")
        # except:
        #     print("Oops! Something wrong")
        return render(request, 'user_app/login.html')

    def post(self, request):
        pass