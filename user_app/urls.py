from django.urls import path
from .import views


app_name = 'user_app'
urlpatterns = [
    path('user_register/', views.UserRegister.as_view(), name='user_register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('job_list', views.job_listing, name='job_list'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('change_password/', views.change_password, name='change_password'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('update_user_profile/', views.update_user_profile, name='update_user_profile'),

  
]
