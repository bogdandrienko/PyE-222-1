from django.urls import path
from django_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

urlpatterns = [
    path("api/public/users_list", views.public_users_list),
    path("api/private/users_list", views.private_users_list, name="private_users_list"),
    path("api/admin/users_list", views.admin_users_list, name="admin_users_list"),
    path("api/our_moderator/users_list", views.our_moderator_users_list, name="our_moderator_users_list"),

    # login MVT
    path("login/", views.f_login, name="login"),
    path("logout/", views.f_logout, name="logout"),

    # JWT(jason web token) authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # drf
    path("api/drf/public/users_list", views.drf_public_users_list),
    path("api/drf/private/users_list", views.drf_private_users_list),
]
