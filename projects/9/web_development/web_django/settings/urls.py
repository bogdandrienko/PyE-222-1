from django.contrib import admin
from django.urls import path, include

urlpatterns = [  # URL GLOBAL
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
]
