from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """Функция-контроллер -
    +гибкая
    -много дублирующегося кода
    """
    return render(request, "django_app/home.html", context={})


class AboutView(TemplateView):
    """Класс-контроллер -
    +все плюсы классов: наследование
    -недостаточно универсален
    """
    template_name = "django_app/about.html"
