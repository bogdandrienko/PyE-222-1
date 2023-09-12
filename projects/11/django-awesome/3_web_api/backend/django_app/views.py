from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


def home(request):
    return HttpResponse("OK")


@csrf_exempt  # - отключает защиту csrf для этого контроллера
def native_django_api(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.body)  # bytes
    # print(request.data)
    return JsonResponse(data={"message": "OK"}, safe=True)


@api_view(http_method_names=["GET", "POST"])
def api(request: Request) -> Response:
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    # print(request.body)
    print(request.data)  # dictionary

    return Response(data={"message": "OK"}, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET", "POST"])  # красивый интерфейс
def messages(request: Request) -> Response:
    if request.method == "GET":
        with open("messages.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        data = {"messages": lines}
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # {"message": "Привет Айгерим!"}
        print(request.GET)
        print(request.POST)
        print(request.FILES)
        # print(request.body)
        print(request.data)  # dictionary

        message: str = request.data.get('message', '')
        with open("messages.txt", "a", encoding="utf-8") as file:
            file.write(f"{message}\n")

        return Response(data={"message": "OK"}, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE", "PATCH"])
def weather(request: Request) -> Response:
    if request.method == "GET":
        return Response(data={"text": "Сегодня отличная погода"}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # {"text": "Сегодня дождь!"}
        message: str = request.data.get('text', '')
        print(message)
        return Response(data={"message": "OK"}, status=status.HTTP_201_CREATED)
