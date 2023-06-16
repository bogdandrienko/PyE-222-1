from django.http import HttpResponse
from django.shortcuts import render


def docs_home(request):
    return render(request, "django_documents/home.html", context={})


def docs_list(request):
    docs = [{"id": x, "name": f"Документ {x}"} for x in range(1, 1000)]
    print(docs)
    return render(request, "django_documents/docs_list.html", context={"docs": docs})


def docs_detail(request):
    return HttpResponse("docs_detail")


def docs_public(request):
    return HttpResponse("docs_public")
