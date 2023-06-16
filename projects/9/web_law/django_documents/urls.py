from django.urls import path
from django_documents import views

urlpatterns = [
    # акты
    path('', views.docs_home, name="docs_home"),



    path('list/', views.docs_list, name="docs_list"),



    # path('search/', views.docs_list, name="docs_search"),
    path('detail/<str:pk>/', views.docs_detail, name="docs_detail"),
    path('public/', views.docs_public, name="docs_public"),
]
