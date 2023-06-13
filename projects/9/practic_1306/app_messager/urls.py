from django.urls import path
from app_messager.views import get, post

urlpatterns = [
    path('messages/', get),
    path('send/', post),
]
