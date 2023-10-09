from django_app import views
from django.urls import path
from django_app import views_a

urlpatterns = [
    path("data/", views.data, name="data"),
    path("", views.rooms, name="rooms"),
    path("<slug:slug>/", views.room, name="room")
]

websocket_urlpatterns = [
    path('ws/<slug:room_name>/', views_a.ChatConsumer.as_asgi())
]
