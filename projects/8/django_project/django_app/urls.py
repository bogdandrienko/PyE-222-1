from django.urls import path
from django_app import views

urlpatterns = [
    #    url     func                   name (уникальная ссылка на этот маршрут)
    path('', views.home),
    path('home/', views.home),
    path('register/', views.register, name="register"),

    # todo USERS #####################################################################################################################################
    path('api/users/import/', views.api_users_import, name="api_users_import"),
    path('api/users/export/', views.api_users_export, name="api_users_export"),

    # path('payment/users/register/', views.all_users, name="all_users"),

    # path('api/users/all/', views.all_users, name="all_users"),
    # path('api/users/import/', views.all_users, name="all_users"),
    # path('api/users/export/', views.all_users, name="all_users"),
    # path('api/users/profile/1/', views.all_users, name="all_users"),
    # path('api_users_register/', views.all_users, name="all_users"),
    # path('api/users/block/', views.all_users, name="all_users"),
    # path('api/users/register/', views.all_users, name="all_users"),
    # path('api/users/register/', views.all_users, name="all_users"),
    # path('api/users/register/', views.all_users, name="all_users"),
]
