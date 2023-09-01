from django.urls import path
from django_app import views

urlpatterns = [
    # base
    path("", views.home, name=""),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),
    path("profile/", views.profile, name="profile"),
    # post
    path("post/list/", views.post_list, name="post_list"),
    path("post/list/simple/", views.post_list_simple, name="post_list_simple"),
    path("post/search/", views.post_search, name="post_search"),
    path("post/detail/<str:pk>/", views.post_detail, name="post_detail"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/update/<str:pk>/", views.home, name="post_update"),
    path("post/hide/<str:pk>/", views.post_hide, name="post_hide"),
    # comments
    path("post/comment/create/<str:pk>/", views.post_comment_create, name="post_comment_create"),
    # ratings
    path("post/rating/<str:pk>/<str:is_like>/", views.post_rating, name="post_rating"),
    # recover
    path("user/password_recover/send/", views.user_password_recover_send, name="user_password_recover_send"),
    path("user/password_recover/login/", views.user_password_recover_send, name="user_password_recover_login"),
]
