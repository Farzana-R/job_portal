from django.contrib import admin
from .models import UserDetails, Favourites, AppliedJobs


admin.site.register(UserDetails)
admin.site.register(Favourites)
admin.site.register(AppliedJobs)