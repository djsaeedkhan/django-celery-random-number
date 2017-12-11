from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^', include("test2.urls"), name="index"),
]
