from django.urls import path

# from django_app.views import home  # , about, ....
from django_app import views

urlpatterns = [
    # path("", home, name="home"),
    path("api/", views.index, name="index"),
    path("", views.home, name="home"),
    path("pricing/", views.pricing, name="pricing"),
]
