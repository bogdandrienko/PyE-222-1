from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path("", views.home),
    path("home/", views.home),
    #
    path("api/", views.api),
    path("messages/", views.messages),
    path("weather/", views.weather),
    #
    # workers
    # REST-API/REST x3
    # GET(many), GET(search), POST,
    path("api/workers/", views.workers),
    # GET(one), DELETE, UPDATE
    path("api/workers/<str:pk>", views.workers_pk),
    # TODO создать вообще один контроллер на всё
    #
    path("api/rating/", views.rating),  # name != не нужны в DRF
    path("api/rating/<str:post_id>", views.rating),  # name != не нужны в DRF
    #
    path("api/report/", views.report),
    path("api/report/<str:point_id>", views.report),
]
