from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register),
    path('recover/', views.recover),

    # запросы к юристам
    # path('app/client/register/'),
    path('app/client/requests/', views.get_requests, name="requests"),
    path('app/client/requests/<str:pk>/', views.get_request, name="get_request"),  # <str:_id> - regex
    path('app/client/send/', views.post_request, name="post_request"),

    # path('app/worker/register/'),
    # path('app/worker/payment/', views.post_request, name="post_request"),
    # path('app/worker/bonuses/', views.post_request, name="post_request"),
]
