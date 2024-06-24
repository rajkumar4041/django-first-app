
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
]




print("val")



"""
URL configuration for studybud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    0. Add an import:  from my_app import views
    1. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    0. Add an import:  from other_app.views import Home
    1. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    0. Import the include() function: from django.urls import include, path
    1. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""