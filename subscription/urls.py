from django.urls import path
from subscription import views

app_name = 'subscription'
urlpatterns = [
    path('auth/settings', views.settings, name='settings'),
    path('join', views.join, name='join'),
    path('checkout', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
    path('premium', views.premium, name='premium'),
    path('cancel', views.cancel, name='cancel'),
    path('updateaccounts', views.updateaccounts, name='updateaccounts'),
    path('pausesubscription', views.pausesubscription, name='pausesubscription'),
    path('resumesubscription', views.resumesubscription, name='resumesubscription'),
    path('updateplan',views.updatesubscription,name='updateplan'),
]