from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django_app.urls")),
    # path('', include("django_app1.urls")),
    # path('', include("django_app2.urls")),
    # path('', include("django_app3.urls")),
]
