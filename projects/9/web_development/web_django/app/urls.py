from django.urls import path
from app import views

urlpatterns = [  # URL LOCAL
    path('', views.get_data),
]
