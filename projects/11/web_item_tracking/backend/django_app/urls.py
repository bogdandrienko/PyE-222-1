from django.urls import path

# from django_app.views import home  # , about, ....
from django_app import views

urlpatterns = [
    # TODO PUBLIC ################################################
    path("", views.home, name=""),
    path("home/", views.home, name="home"),
    path("api/", views.index, name="index"),
    path("pricing/", views.pricing, name="pricing"),
    path("help/", views.home, name="help"),
    path("salary/", views.home, name="salary"),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("login/", views.login_, name="login"),
    path("complaint/", views.complaint, name="complaint"),
    # TODO PUBLIC ################################################
    # TODO PRIVATE ###############################################
    path("currency/", views.currency, name="currency"),
    path("coins/", views.coins, name="coins"),
    path("news/", views.news, name="news"),
    path("sms/", views.sms, name="sms"),
    path("logout/", views.logout_, name="logout"),
    # TODO PRIVATE ###############################################
    #
    path("track/start/", views.track_start, name="track_start"),
    path("track/middle/", views.track_start, name="track_middle"),
    path("track/end/", views.track_start, name="track_end"),
    path("track/find/", views.track_find, name="track_find"),
]
