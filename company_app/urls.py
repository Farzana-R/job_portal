from django.urls import path
from .import views

app_name = 'company_app'
urlpatterns = [
    path('company_register/', views.CompanyRegister.as_view(), name='company_register'),
    path('login/', views.Login.as_view(), name='login'),
    path('company_home', views.Home.as_view(), name='company_home'),
    path('company-profile/', views.CompanyProfile.as_view(), name='company_profile'),
    path('update-company-profile/', views.UpdateCompanyProfile.as_view(), name='update_company_profile'), 
]






