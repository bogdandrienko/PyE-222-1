from django.urls import path
from django_app import views

urlpatterns = [
    #     url     # def     # alias
    path('', views.home, name=""),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
]
