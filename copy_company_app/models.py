from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user')
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


    
class Job(models.Model):
    job_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    area_of_job = models.CharField(max_length=250)
    posting_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('job_name',)
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

    def __str__(self):
        return '{}'.format(self.job_name)

