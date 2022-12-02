from django.db import models
from django.contrib.auth.models import User

from company_app.models import Job

# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True)
    # gender
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, unique=True)
    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    description = models.TextField(blank=True) 

    def __str__(self):
        return '{}'.format(self.user.first_name)
    # def __str__(self):
    #     return self.user.username


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    job = models.ForeignKey(Job, on_delete = models.CASCADE)

    def __str__(self):
        return (str(self.user)+ str(self.job))