from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [   
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='commons/change-password.html',
        success_url = '/'), name='change_password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='commons/password-reset/password_reset.html',
        subject_template_name='commons/password-reset/password_reset_subject.txt',
        email_template_name='commons/password-reset/password_reset_email.html',
        success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='commons/password-reset/password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='commons/password-reset/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='commons/password-reset/password_reset_complete.html'), 
        name='password_reset_complete'),
]