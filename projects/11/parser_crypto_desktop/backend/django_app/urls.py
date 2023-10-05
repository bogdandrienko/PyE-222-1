from django.urls import path
from django_app import views


urlpatterns = [
    path("news/", views.news),
    path("weather/", views.weather),
]
