from django.urls import path
from django_app import views

urlpatterns = [
    # base
    path('', views.home, name="home"),
    path('login/', views.login_f, name="login"),
    path('logout/', views.logout_f, name="logout"),
    path('register/', views.register_f, name="register"),

    # posts
    path('list/', views.post_list, name="posts"),
    path('create/', views.post_create, name="post_create"),
    path('detail/<str:pk>/', views.post_detail, name="post_detail"),
    path('change/<str:pk>/', views.post_change, name="post_change"),
    path('delete/<str:pk>/', views.post_delete, name="post_delete"),

    # post comments
    path('comment/create/<str:pk>/', views.post_comment_create, name="post_comment_create"),

    # post ratings
    path('rating/change/<str:pk>/<str:status>/', views.rating_change, name="rating_change"),

    # TODO
    path('about/', views.home, name="about"),
    path('contacts/', views.home, name="contacts"),
    path('profile/', views.home, name="profile"),
]
