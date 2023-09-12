from django.http import HttpRequest, HttpResponse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "django_app/home.html", context=context)
