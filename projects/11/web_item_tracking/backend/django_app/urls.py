from django.urls import path

# from django_app.views import home  # , about, ....
from django_app import views

urlpatterns = [
    # path("", home, name="home"),
    path("api/", views.index, name="index"),
    path("", views.home, name="home"),
    path("currency/", views.currency, name="currency"),
    path("coins/", views.coins, name="coins"),
    path("news/", views.news, name="news"),
    #
    # TODO ################################################
    path("pricing/", views.pricing, name="pricing"),
    path("sms/", views.sms, name="sms"),
    # TODO ################################################
    #
]
