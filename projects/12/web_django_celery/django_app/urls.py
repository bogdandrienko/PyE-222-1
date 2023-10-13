from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home, name="home"),

    path('books/', views.books, name="books"),
    path('celer/', views.celer, name="celer"),
    path('start/', views.start, name="start"),
]
