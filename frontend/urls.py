from django.urls import path
from .views import home, registration, login, forgotpassword 



urlpatterns = [   
    path('', home),
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('forgotpassword/', forgotpassword, name='forgotpassword'),
]
