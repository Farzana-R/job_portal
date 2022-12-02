
from django.contrib import messages, auth
from django.conf import settings
from django.shortcuts import HttpResponseRedirect, render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from company_app.models import Job
from user_app.models import UserDetails, Favourites

from . import forms


class UserDashboard(View):
    def get(self, request):
        jobs = Job.objects.all()
        return render(request, 'user_app/user_dashboard.html', {'jobs' : jobs})


class JobListing(View):
    def get(self, request):
        jobs = Job.objects.all()
        return render(request, 'user_app/job_list.html', {'jobs' : jobs})

    
class JobDetail(View):
    def get(self, request, job_id):
        job_detail = Job.objects.get(id=job_id)
        return render(request, 'user_app/job-detail.html', {'job_detail':job_detail})


# save a job
@login_required
def save_job(request, slug):
    user = request.user
    job = get_object_or_404(Job, slug=slug)
    saved, created = Favourites.objects.get_or_create(job=job, user=user)
    return redirect('user_app:favourites-job')
    # return HttpResponseRedirect('/job/{}'.format(job.slug))


# saved job view
def favourites(request):
    saved_jobs = Favourites.objects.filter(user=request.user)
    return render(request, 'user_app/saved_job.html', {'saved_jobs':saved_jobs})

# delete saved jobs
def saved_job_delete(request, job_id):
    Favourites.objects.get(id=job_id).delete()
    saved_jobs = Favourites.objects.filter(user=request.user)
    return render(request, 'user_app/saved_job.html', {'saved_jobs':saved_jobs})


# view profile
@method_decorator(login_required, name='get')
class UserProfile(View):
    def get(self, request):
        user_details = UserDetails.objects.get(user=request.user)
        print(user_details.image)
        return render(request, 'user_app/view_user_profile.html', {'user_details': user_details})


# edit profile
@method_decorator(login_required, name='get')
class UpdateUserProfile(View):
    def get(self, request):
        form = forms.UserUpdateProfileForm()
        return render(request, 'user_app/edit_profile.html', {'form': form})

    def post(self, request):
        profile = UserDetails.objects.filter(user=request.user).first()
        form = forms.UserUpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_app:user_profile')
        else:
            return render(request, 'user_app/edit_profile.html', {'form': form})




class UserRegister(View):
    def get(self, request):
        user_form = forms.UserRegisterForm()
        context = {'form' : user_form}
        return render(request, 'user_app/register.html', context)

    def post(self, request):
        user_form = forms.UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            # Sending  mail to registered user
            email=user_form.cleaned_data['email']             
            send_mail('HI WELCOME ...',
                'Hi welcome to JOBRIAL',
                settings.EMAIL_HOST_USER, [email], fail_silently=False)
            return redirect('user_app:login')

        context = {'form' : user_form}
        return render(request, 'user_app/register.html', context)


class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        context={'form': form}
        return render(request, 'user_app/login.html', context)
    
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
        return render(request, 'user_app/login.html', context)