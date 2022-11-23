from django.urls import path
from . import views


app_name = 'user_app'
urlpatterns = [
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('job_list', views.job_listing, name='job_list'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('favourites-job/', views.favourites, name='favourites-job'),
    path('saved_job_delete/<int:job_id>/', views.saved_job_delete, name='saved_job_delete'),
  
]
