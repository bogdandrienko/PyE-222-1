from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.register),
    path("register/", views.register, name="register"),
]
