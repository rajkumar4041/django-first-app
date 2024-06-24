from django.urls import path
from . import views

"""
Merge with unrelated histories
"""
urlpatterns=[
    path('',views.home,name="home"),
    path('room/',views.room,name="room")
]
