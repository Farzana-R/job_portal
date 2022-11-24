from django.urls import path
from . import views 


urlpatterns = [   
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('user-register/', views.UserRegister.as_view(),\
         name='user_register'),
    path('company-register/', views.CompanyRegister.as_view(),\
         name='company_register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('about/', views.about,name='about'),
]