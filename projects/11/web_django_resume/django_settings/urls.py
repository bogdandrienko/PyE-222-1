from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("", include("django_app.urls")),
]
