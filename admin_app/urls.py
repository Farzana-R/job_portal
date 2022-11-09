from django.urls import path
from . import views 



urlpatterns = [   
    # path('', views.home,name='home'),
    path('', views.Home.as_view(),name='home'),
    path('user_register/', views.user_register, name='user_register'),
    path('company_register/', views.company_register, name='company_register'),
    path('loginview/', views.loginview, name='login'),
    path('logout',views.logout,name='logout'),

    # path('registration/', registration, name='registration'),
    # path('forgotpassword/', forgotpassword, name='forgotpassword'),
]
