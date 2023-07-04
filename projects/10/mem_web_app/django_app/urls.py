from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name=""),
    path("index/", views.home, name="index"),
    path("home/", views.home, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    #
    path("list/", views.list_view, name="list"),
    path("list/", views.list_view, name="posts"),
    path("detail/<str:pk>/", views.detail_view, name="post_detail"),
    path("detail/<str:pk>/", views.detail_view, name="post_change"),
    path("detail/<str:pk>/", views.detail_view, name="post_delete"),
    #
    path("detail/<str:pk>/", views.detail_view, name="detail"),
    path("create/", views.create_view, name="create"),
]
