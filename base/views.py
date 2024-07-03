from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# Create your views here.
# FUTURE reference
# rooms = [
#     {"id": 1, "name": "learn django"},
#     {"id": 2, "name": "learn react"},
#     {"id": 3, "name": "learn mern Stack"},
# ]


def home(request):
    # rooms is coming From DB `Room` table (Model)
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    # FUTURE reference
    # for it in rooms:
    #     if it["id"] == int(pk):
    #         room = it
    room = Room.objects.get(id=pk)
    context = {"room": room}

    return render(request, "base/room.html", context)


def home_room(request):
    context = {"room": room}
    return render(request, "base/room.html", context)


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        # post data of form
        print("form data ", request.POST)
        form = RoomForm(request.POST)
        # we can get one by one value and save them as well
        # @Example: request.POST.get("name"),request.POST.get("description")
        # we dont need to do that manually just bcz we are using modern form

        # check the basic validation for form  and save the form
        if form.is_valid:
            form.save()
            # because we have name `home` in url.py ( path )
            # we can directly pass the name home here
            return redirect("home")

    content = {"form": form}
    return render(request, "base/room_form.html", content)
