from django.urls import path
from . import views
"""
test
"""

urlpatterns=[
    path('',views.home,name="home"),
    path('room/',views.room,name="room" )
]
