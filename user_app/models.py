from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='user_images', blank=True)
    description = models.TextField(blank=True) 