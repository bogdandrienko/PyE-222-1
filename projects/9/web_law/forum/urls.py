from django.urls import path
from forum import views

urlpatterns = [
    path('forum/', views.home, name="forum_home"),
    path('forum/', views.home, name="forum_register"),
    path('forum/', views.home, name="forum_login"),
    path('forum/posts/', views.posts, name="forum_list"),
    path('forum/', views.home, name="forum_post"),
]
