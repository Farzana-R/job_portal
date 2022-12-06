from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View
from django.utils.decorators import method_decorator

from company_app.models import Job
from . import forms
from . models import UserDetails


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


@method_decorator(login_required, name='get')
class UserProfile(View):
    def get(self, request):
        user_details = UserDetails.objects.get(user=request.user)
        return render(request, 'user_app/view_user_profile.html', {'user_details': user_details})


# @method_decorator(login_required, name='get')
# class UpdateUserProfile(View):
#     def get(self, request):
#         form = forms.UserUpdateProfileForm()
#         return render(request, 'user_app/edit_profile.html', {'form': form})

#     def post(self, request):
#         profile = UserDetails.objects.filter(user=request.user).first()
#         form = forms.UserUpdateProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('user_profile')
#         else:
#             return render(request, 'user_app/edit_profile.html', {'form': form})

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
            #return render(request, 'user_app/edit_profile.html', {'form': form})
            return render(request, 'user_app/view_user_profile.html', {'user_details': profile})
            return redirect('user_profile')
        else:
            return render(request, 'user_app/edit_profile.html', {'form': form})
   