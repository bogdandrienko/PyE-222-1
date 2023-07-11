from django.urls import path
from django_app import views

urlpatterns = [
    # главная страница
    path("", views.home, name=""),
    path("index/", views.home, name="index"),
    path("home/", views.home, name="home"),

    # страница регистрации
    path("register/", views.register_view, name="register"),

    # страница авторизации
    path("login/", views.login_view, name="login"),

    # страница выхода из аккаунта
    path("logout/", views.logout_view, name="logout"),

    # страница для показа всех мемов
    path("list/", views.list_view, name="list"),

    #
    path("list/", views.list_view, name="posts"),
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
