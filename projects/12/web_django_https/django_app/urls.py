from django.urls import path
from django_app import views

urlpatterns = [
    # base
    path("", views.home, name=""),
    path("home/", views.home, name="home"),
]
