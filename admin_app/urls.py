from django.urls import path
from . import views 



urlpatterns = [   
    path('', views.Home.as_view(),name='home'),
    path('about/', views.About.as_view(),name='about'),
    path('contact/', views.Contact.as_view(),name='contact'),
    path('user_register/', views.UserRegister.as_view(), name='user_register'),
    path('company_register/', views.CompanyRegister.as_view(), name='company_register'),
    path('loginview/', views.loginview, name='loginview'),
    path('logout',views.logout,name='logout'),
    # path('about/', views.about,name='about'),
]
