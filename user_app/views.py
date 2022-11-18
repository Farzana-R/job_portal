from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from . models import UserDetails
from company_app.models import Job


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



# user profile
# @login_required
# def user_profile(request):
#     you = request.user
#     profile = Profile.objects.filter(user=you).first()
#     user_skills = Skill.objects.filter(user=you)
#     if request.method == 'POST':
#         form = NewSkillForm(request.POST)
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.user = you
#             data.save()
#             return redirect('my-profile')
#     else:
#         form = NewSkillForm()
#     context = {
#         'u': you,
#         'profile': profile,
#         'skills': user_skills,
#         'form': form,
#         'profile_page': "active",
#     }
#     return render(request, 'candidates/profile.html', context)

# edit profile
# @login_required
# def edit_profile(request):
#     you = request.user
#     profile = Profile.objects.filter(user=you).first()
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             data = form.save(commit=False)
#             data.user = you
#             data.save()
#             return redirect('my-profile')
#     else:
#         form = ProfileUpdateForm(instance=profile)
#     context = {
#         'form': form,
#     }
#     return render(request, 'candidates/edit_profile.html', context)

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
    