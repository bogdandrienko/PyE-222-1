from django.urls import path
from django_app import views


urlpatterns = [
    path("weather/", views.weather),
]
