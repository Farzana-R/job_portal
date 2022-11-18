from django.contrib import admin
from .models import Company, Job



# admin.site.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Company,CompanyAdmin)

# admin.site.register(Job)

class JobAdmin(admin.ModelAdmin):
    list_display = ['job_name','slug']
    prepopulated_fields = {'slug':('job_name',)}
admin.site.register(Job,JobAdmin)

