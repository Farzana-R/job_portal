from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# from autoslug import AutoSlugField

# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=250, default='name')
    slug = models.SlugField(max_length=250, unique=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=250, unique=True)
    logo = models.ImageField(upload_to='company_logos', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return '{}'.format(self.user)


CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)

    
class Job(models.Model):
    job_name = models.CharField(max_length=250)
    # slug = AutoSlugField(populate_from='job_name', unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True, null=True)
    skills_req = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    benifits = models.TextField(blank=True, null=True)
    job_type = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True, blank=True)
    posting_date = models.DateTimeField(auto_now_add=True)
    area_of_job = models.CharField(max_length=250)
    
    class Meta:
        ordering = ('job_name',)
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

    def __str__(self):
        return '{}'.format(self.job_name)


class Applicants(models.Model):
    job = models.ForeignKey(
        Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(
        Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant

    

