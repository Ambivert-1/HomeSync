"""IOTApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')),
"""
from django.contrib import admin
from django.urls import path

from . import functions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", functions.homepage, name="home"),
    path("lighton/", functions.lighton, name="lighton"),
    path("lightoff/", functions.lightoff, name="lightoff"),
    path("OnRelay1/", functions.relay_on_7, name=""),
    path("OFFRelay1/", functions.relay_off_7, name=""),
    path("OnRelay2/", functions.relay_on_6, name=""),
    path("OFFRelay2/", functions.relay_off_6, name=""),
    path("OnRelay3/", functions.relay_on_5, name=""),
    path("OFFRelay3/", functions.relay_off_5, name=""),
    path("OnRelay4/", functions.relay_on_4, name=""),
    path("OFFRelay4/", functions.relay_off_4, name=""),
    path("AllOFF/", functions.turn_off_all_relay),
    path("AllON/", functions.turn_on_all_relay),
]
