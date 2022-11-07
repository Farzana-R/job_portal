from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    address = models.TextField(unique=True)
    phone_number = models.IntegerField(unique=True)
    logo = models.ImageField(upload_to='company_logos', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    
class Job(models.Model):
    job_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    area_of_job = models.CharField(max_length=250)
    posting_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('job_name',)
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

