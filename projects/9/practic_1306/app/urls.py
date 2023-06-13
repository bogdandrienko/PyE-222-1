from django.urls import path
from app.views import get_data, get_string,get_json

urlpatterns = [
    path('string/', get_string),
    path('json/', get_json),
    path('', get_data),
]
