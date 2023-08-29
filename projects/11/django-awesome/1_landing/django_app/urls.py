from django.urls import path
from django_app.views import home, AboutView

urlpatterns = [
    path("", home, name=""),
    path("home/", home, name="home"),
    path("about/", AboutView.as_view(), name="about"),
]

