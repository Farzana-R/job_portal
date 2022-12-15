from django.urls import path

from . import views

app_name = 'chat_app'
urlpatterns = [
    path("room/", views.Room.as_view(), name="room"),
    path("<str:room_name>/", views.ChatRoom.as_view(), name="chat_room"),
    
]