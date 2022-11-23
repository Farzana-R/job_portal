from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
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

    # Change Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='commons/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password-reset/password_reset.html',
             subject_template_name='commons/password-reset/password_reset_subject.txt',
             email_template_name='commons/password-reset/password_reset_email.html',
             #success_url=reverse_lazy('loginview')
             success_url=reverse_lazy('password_reset_done')
             #success_url='/loginview/'
             #success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]
