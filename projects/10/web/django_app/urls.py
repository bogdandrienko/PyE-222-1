"""Маршруты(URL) - ССЫЛКИ"""

from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name=""),
    path("index/", views.home, name="index"),
    path("home/", views.home, name="home"),

    path("register/", views.register, name="register"),
    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),

    path("list/", views.list, name="list"),

    # news
    path("news/list/", views.news_list, name="news_list"),
    path("news/detail/<str:pk>/", views.news_detail, name="news_detail"),
    path("news/comments/create/<str:pk>/", views.news_comments_create, name="news_comments_create"),
    path('rating/change/<str:pk>/<str:status>/', views.rating_change, name="rating_change"),

    #
    #
    #
    #
    #
    #
    path("list/", views.list, name="posts"),
    path("detail/<str:pk>/", views.detail_view, name="post_detail"),
    path("detail/<str:pk>/", views.detail_view, name="post_change"),
    path("detail/<str:pk>/", views.detail_view, name="post_delete"),
    #
    path("detail/<str:pk>/", views.detail_view, name="detail"),
    path("create/", views.create_view, name="create"),
    # SELECT - GET
    path("list_memes/", views.list_memes, name="list_memes"),
    # INSERT - POST
    path("create_mem/", views.create_mem, name="create_mem"),
    # UPDATE - PUT/PATCH
    path("update_mem/<str:pk>/", views.update_mem, name="update_mem"),
    # DELETE - DELETE
    path("delete_mem/<str:pk>/", views.delete_mem, name="delete_mem"),
]
