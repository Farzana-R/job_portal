from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View

from user_app.models import UserDetails

from . import forms
from company_app.models import Applicants, Company, Job, Selected


class Home(View):
    def get(self, request):
        return render(request, 'company_app/company_home.html')


# to select a candidate
@login_required
def select_applicant(request, can_id, job_id):
    job = get_object_or_404(Job, slug=job_id)
    profile = get_object_or_404(UserDetails, slug=can_id)
    user = profile.user
    selected, created = Selected.objects.get_or_create(job=job, applicant=user)
    applicant = Applicants.objects.filter(job=job, applicant=user).first()
    applicant.delete()
    return redirect('company_app:selected_list')
    # return HttpResponseRedirect('/hiring/job/{}/applicants'.format(job.slug))


# to remove an applicant
@login_required
def remove_applicant(request, can_id, job_id):
    job = get_object_or_404(Job, slug=job_id)
    profile = get_object_or_404(UserDetails, slug=can_id)
    user = profile.user
    applicant = Applicants.objects.filter(job=job, applicant=user).first()
    applicant.delete()
    return redirect('company_app:remove_applicant')
    # return HttpResponseRedirect('/hiring/job/{}/applicants'.format(job.slug))


# selected candidates
@login_required
def selected_list(request, slug):
    job = get_object_or_404(Job, slug=slug)
    selected = Selected.objects.filter(job=job).order_by('date_posted')
    profiles = []
    for applicant in selected:
        profile = UserDetails.objects.filter(user=applicant.applicant).first()
        profiles.append(profile)
    context = {
        'profiles': profiles,
        'job': job,
    }
    return render(request, 'company_app/selected_list.html', context)


# to list all applicants
@login_required
def applicant_list(request, slug):
    job = get_object_or_404(Job, slug=slug)
    applicants = Applicants.objects.filter(job=job).order_by('date_posted')
    profiles = []
    for applicant in applicants:
        profile = UserDetails.objects.filter(user=applicant.applicant).first()
        profiles.append(profile)
    context = {
        'profiles': profiles,
        'job': job,
    }
    print(9)
    return render(request, 'company_app/applicant_list.html', context)


# to display all jobs
@login_required
def all_jobs(request):
    company=Company.objects.get(user=request.user)
    jobs = Job.objects.filter(company=company).order_by('posting_date')
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj,}
    return render(request, 'company_app/job_list.html', context)


# job detailed page
@login_required
def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    context = {
        'job': job,
        
    }
    print(request.user)
    print(job.company)
    return render(request, 'company_app/job_detail.html', context)


# add job
@login_required
def add_job(request):
    user = request.user
    company=Company.objects.get(user=user)
    # print(Job.objects.get(company=company))
    
    if request.method == "POST":
        form = forms.NewJobForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.company = company
            data.slug = data.job_name
            data.save()
            return redirect('company_app:all_jobs')
    else:
        form = forms.NewJobForm()
    context = {'form': form,}
    return render(request, 'company_app/add_job.html', context)


# edit job
@login_required
def edit_job(request, slug):
    user = request.user
    job = get_object_or_404(Job, slug=slug)
    if request.method == "POST":
        form = forms.NewJobForm(request.POST, instance=job)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('company_app:add-job-detail', slug)
    else:
        form = forms.NewJobForm(instance=job)
    context = {
        'form': form,
        'job': job,
    }
    return render(request, 'company_app/edit_job.html', context)


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


# register a new company
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


# login for company
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


class ChatRoom(View):
    def get(self, request, room_name):
        context={'room_name': room_name}
        return render(request, 'company_app/chat_room.html', context)
