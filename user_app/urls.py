from django.urls import path
from .import views


urlpatterns = [
    path('user-dashboard/', views.UserDashboard.as_view(), name='user_dashboard'),
    path('job-list/', views.JobListing.as_view(), name='job_list'),
    path('job-detail/<int:job_id>/', views.JobDetail.as_view(), name='job_detail'),
    path('user-profile/', views.UserProfile.as_view(), name='user_profile'),
    path('update-user-profile/', views.UpdateUserProfile.as_view(), name='update_user_profile'), 
]