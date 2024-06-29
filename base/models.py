from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    # below some commented var are for later used
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=80)

    # null = true is for db that this is an optional field
    # blank = true is for form that we can submit form without fill this field
    description = models.TextField(null=True, blank=True)
    # participants =

    # auto now is for every time save the form give the date time of that particular save date time
    updated = models.DateTimeField(auto_now=True)

    # auto now add is give the only one time date time when we save the form first time
    created = models.DateTimeField(auto_now_add=True)

    # necessary to create a string version
    # it just what we wanna return
    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    # user =
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]
