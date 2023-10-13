from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home),
    path("home/", views.home),
    path("create/", views.create),
]
