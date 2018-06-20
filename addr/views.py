from django.shortcuts import render
from django.utils import timezone
from .models import Friend

def friend_list(request):
    friends = Friend.objects.all()
    return render(request, 'addr/friend_list.html', {'friends': friends })