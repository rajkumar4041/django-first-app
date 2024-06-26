from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {"id": 1, "name": "learn django"},
    {"id": 2, "name": "learn react"},
    {"id": 3, "name": "learn mern Stack"},
]


def home(request):
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = None
    for it in rooms:
        if it["id"] == int(pk):
            room = it

    context = {"room": room}

    return render(request, "base/room.html", context)
