from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from autoslug import AutoSlugField
# from django_countries.fields import CountryField


from company_app.models import Job

# Create your models here.

CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # slug = AutoSlugField(populate_from='user', unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    address = models.TextField(blank=True, null=True)
    # country = CountryField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, unique=True)
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    description = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    grad_year = models.IntegerField(blank=True, null=True)
    looking_for = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.user.first_name)


class Skill(models.Model):
    skill = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, related_name='skills', on_delete=models.CASCADE)


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    job = models.ForeignKey(Job, on_delete = models.CASCADE)

    def __str__(self):
        return (str(self.user)+str('-->')+str(self.job))


class AppliedJobs(models.Model):
    job = models.ForeignKey(
        Job, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.job_name