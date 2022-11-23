from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from company_app.models import Job


from . import forms
from . models import UserDetails



def user_dashboard(request):
    jobs = Job.objects.all()
    return render(request, 'user_app/user_dashboard.html', {'jobs' : jobs})


# to list all jobs
def job_listing(request):
    jobs = Job.objects.all()
    return render(request, 'user_app/job_list.html', {'jobs' : jobs})

def job_detail(request, job_id):
    job_detail = Job.objects.get(id=job_id)
    return render(request, 'user_app/job-detail.html', {'job_detail':job_detail})


def change_password(request):
    return render(request, 'user_app/change_password.html')


# user profile
@login_required
def user_profile(request):
    users = request.user
    user_details = UserDetails.objects.get(user=users)
    return render(request, 'user_app/view_user_profile.html', {'user_details': user_details})


# edit
@login_required
def update_user_profile(request):
    you = request.user
    profile = UserDetails.objects.filter(user=you).first()
    if request.method == "POST":
        form = forms.UserUpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_app:user_profile')
    else:
        form = forms.UserUpdateProfileForm(instance=profile)
        form = forms.UserUpdateProfileForm()


    context = {'form': form}
    return render(request, 'user_app/edit_profile.html', context)



# profile view for recruters
# @login_required
# def profile_view(request, slug):
#     p = Profile.objects.filter(slug=slug).first()
#     you = p.user
#     user_skills = Skill.objects.filter(user=you)
#     context = {
#         'u': you,
#         'profile': p,
#         'skills': user_skills,
#     }
#     return render(request, 'candidates/profile.html', context)


# def candidate_details(request):
#     return render(request, 'candidates/details.html')
    