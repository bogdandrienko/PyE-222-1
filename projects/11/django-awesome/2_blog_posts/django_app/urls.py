from django.urls import path
from django_app import views

urlpatterns = [
    # base
    path("", views.home, name=""),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),
    # post
    path("post/list/", views.post_list, name="post_list"),
    path("post/search/", views.post_search, name="post_search"),
    path("post/detail/<str:pk>/", views.home, name="post_detail"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/update/<str:pk>/", views.home, name="post_update"),
    path("post/delete/<str:pk>/", views.home, name="post_delete"),
    # comments
    # path("post/delete/<str:pk>/", views.home, name="post_delete"),
    # ratings
    # path("post/delete/<str:pk>/", views.home, name="post_delete"),
]
