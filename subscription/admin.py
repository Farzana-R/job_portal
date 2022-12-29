from django.contrib import admin

from subscription.models import Customer, CustomerStatus

admin.site.register(Customer)
admin.site.register(CustomerStatus)
