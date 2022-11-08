from django.urls import path
from .views import (UserRegistration, UserLogin)


urlpatterns = [
    path('registration/', UserRegistration.as_view(), name = 'user_registration'),
    path('login/', UserLogin.as_view(), name = 'user_login'),
  
]
