from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.register),
    path("register_mvt/", views.register_mvt, name="register_mvt"),
    path("register/", views.register, name="register"),
    #
    path("resume_mvt/list/", views.resume_list_mvt, name="resume_list_mvt"),
    path("resume/list/", views.resume_list),
]
