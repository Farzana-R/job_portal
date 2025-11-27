from django.urls import path
from .import views

app_name = 'user_app'
urlpatterns = [
    path('user-register/', views.UserRegister.as_view(),\
        name='user_register'),
    path('login/', views.Login.as_view(), name='login'),
    path('job-list/', views.JobListing.as_view(), name='job_list'),
    path('job-detail/<int:job_id>/', views.JobDetail.as_view(), name='job_detail'),
    path('user-profile/', views.UserProfile.as_view(), name='user_profile'),
    path('update-user-profile/', views.UpdateUserProfile.as_view(), name='update_user_profile'),

    path('favourites-job/', views.favourites, name='favourites-job'),
    path('job/<slug>/save/', views.save_job, name='save-job'),
    path('saved_job_delete/<int:job_id>/', views.saved_job_delete, name='saved_job_delete'),

    path('apply-job/<int:job_id>/', views.apply_job, name='apply-job'),
    path('user-dashboard/', views.UserDashboard.as_view(), name='user_dashboard'),

    path('profile/<slug>', views.profile_view, name='profile_view'),

]