from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {
        'title': 'Chat Selection',
    }
    return render(request, 'chat/index.html', context=context)


@login_required
def room(request, room_name):
    context = {
        'title': room_name,
        'room_name': room_name,
    }
    return render(request, 'chat/room.html', context=context)
