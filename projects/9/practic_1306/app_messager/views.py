from django.shortcuts import render


def get(request):
    with open("data.txt", mode="r", encoding="utf-8") as file:
        list1 = file.readlines()
    return render(request, "messages.html", context={"list1": list1})


def post(request):
    pass
