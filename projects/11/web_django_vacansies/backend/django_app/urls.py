from django.urls import path
from django_app import views

urlpatterns = [
    path("api/", views.api),
    path("", views.index),
    path("api/vacasies/", views.vacasies),
    #
    path("api/blank/", views.blank),
    path("api/best_seller/", views.best_seller),
]
