from django.urls import path
from .import views

app_name = 'company_app'
urlpatterns = [
path('company-register/', views.CompanyRegister.as_view(),\
        name='company_register'),
path('login/', views.Login.as_view(), name='login'),
]






