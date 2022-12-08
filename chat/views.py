from django.shortcuts import render
from django.views.generic import View

from company_app.models import Company
from user_app.models import UserDetails


class Room(View):
    def get(self, request):
        company = Company.objects.all().exclude(user=request.user.id)
        users = UserDetails.objects.all().exclude(user=request.user.id)
        context={'company': company, 'users':users}
        return render(request, "chat/room.html", context)


class ChatRoom(View):
    def get(self, request, room_name):
        context={'room_name': room_name}
        return render(request, 'chat/chat_room.html', context)
