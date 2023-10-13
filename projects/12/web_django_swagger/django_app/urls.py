from django.contrib import admin
from django.urls import path, include
from django_app import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # автодокументация
    path("api/swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("api/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # TODO news ###########################################
    # GET(many) POST
    # path("api/news/", views.news_f, name="news"),
    # GET(one) PUT(PATCH) DELETE
    # path("api/news/<str:news_id>", views.news_id_f, name="news_id"),
    # TODO news ###########################################
    #
    # path("", views.home),
    # path("home/", views.home),
    #
    # path("api/", views.api),
    # path("messages/", views.messages),
    # path("weather/", views.weather),
    # #
    # # workers
    # # REST-API/REST x3
    # # GET(many), GET(search), POST,
    # path("api/workers/", views.workers),
    # # GET(one), DELETE, UPDATE
    # path("api/workers/<str:pk>", views.workers_pk),
    # # TODO создать вообще один контроллер на всё
    # #
    # path("api/rating/", views.rating),  # name != не нужны в DRF
    # path("api/rating/<str:post_id>", views.rating),  # name != не нужны в DRF
    # #
    # path("api/report/", views.report),
    # path("api/report/<str:point_id>", views.report),
    #
    #
    #
    #
    #
    path("api/news/list/", views.news_list, name="news_list"),
    path("api/news/create/", views.news_create, name="news_create"),
]
