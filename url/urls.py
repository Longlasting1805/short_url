from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('createshorturl', views.createshorturl, name="createshorturl"),
    path("urlcreated", views.urlcreated, name="urlcreated")
]
