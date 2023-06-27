from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home),
    path('list/', views.post_list, name="posts"),
    path('create/', views.post_create, name="post_create"),

    path('delete/<str:pk>/', views.post_delete, name="post_delete"),
    path('detail/<str:pk>/', views.post_detail, name="post_detail"),
    path('change/<str:pk>/', views.post_change, name="post_change"),

    path('comment/create/<str:pk>/', views.post_comment_create, name="post_comment_create"),
    path('rating/like/<str:pk>/', views.rating_like, name="rating_like"),
    path('rating/dislike/<str:pk>/', views.rating_dislike, name="rating_dislike"),


    path('', views.home, name="post_list_post"),
]
