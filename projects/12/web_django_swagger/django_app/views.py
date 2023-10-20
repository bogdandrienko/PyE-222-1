import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from django_app import models, serializers

# https://github.com/bogdandrienko/django_drf_react_typescripts_facebook_app/blob/main/backend/django_api/views.py
# 1) Упрощённый - просто подключили библиотеку для swagger
# 2) Продвинутый - нужно "описывать" для каждой функции значения на входе и на выходе.

response_schema_dict = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
                "200_key1": "200_value_1",
                "200_key2": "200_value_2",
            }
        },
    ),
    "205": openapi.Response(
        description="custom 205 description",
        examples={
            "application/json": {
                "205_key1": "205_value_1",
                "205_key2": "205_value_2",
            }
        },
    ),
    "205": openapi.Response(
        description="custom 205 description",
        examples={
            "application/json": {
                "205_key1": "205_value_1",
                "205_key2": "205_value_2",
            }
        },
    ),
}


# TODO news ###########################################
# @swagger_auto_schema(responses=response_schema_dict, methods=["GET", "POST"])
@api_view(http_method_names=["GET", "POST"])  # GET(many) POST
def news_f(request: Request) -> Response:
    """
    * GET(many) - получить все новости из базы данных
    - кэш, пагинация, поиск, сортировка, фильтрация...

    * POST - получить из JSON новость и записать её в базу
    - {"title"(unique): "Новость 1"}
    """

    if request.method == "GET":
        # # плавающий "баг"
        # int1 = random.randint(1, 2)
        # if int1 % 2 == 0:
        #     raise Exception("Ошибка Базы данных")

        data = []
        for i in range(1, 100):
            new = {"id": i, "title": f"Новость {i}"}
            data.append(new)
        return Response(data={"list": data, "message": "OK"}, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="POST",
    request_body=serializers.NewsSerializer,  # Описание входных данных
    responses={201: "Успех", 400: "Error detail"},  # Описание выходных данных
)
@api_view(http_method_names=["POST"])
def news_create(request: Request) -> Response:
    """
    Отправка формы с новостью.

    JSON -> DB
    """
    try:
        title = request.data["title"]  # json form
        description = request.data.get("description", "")  # json form
        models.News.objects.create(title=title, description=description)  # ORM
        return Response(data={"message": "Успех"}, status=status.HTTP_201_CREATED)
    except Exception as error:
        return Response(data=f"ERROR: {error}", status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(  # документация
    method="GET",
    manual_parameters=[
        openapi.Parameter("search_by", openapi.IN_QUERY, description="Поиск по этому параметру", type=openapi.TYPE_STRING, default="")
    ],  # Описание входных данных
    responses={200: serializers.NewsSerializer, 400: "Error detail"},  # Описание выходных данных
)
@api_view(http_method_names=["GET"])
def news_list(request: Request) -> Response:
    """
    Возврат списка новостей.

    * поиск
    * сортировка
    * фильтрация(категория)
    * страница
    * лимит
    * кэш(да/нет)

    DB -> Python -> JSON
    """
    try:
        search_by = request.query_params.get("search_by", "")  # query params
        news_objs = models.News.objects.filter(title__icontains=search_by)  # DB -> Python
        news_jsons = serializers.NewsSerializer(news_objs, many=True).data  # Python -> JSON
        return Response(data=news_jsons, status=status.HTTP_200_OK)
    except Exception as error:
        return Response(data=f"ERROR: {error}", status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE"])  # GET(one) PUT(PATCH) DELETE
def news_id_f(request: Request, news_id: str) -> Response:
    news_id: int = int(news_id)
    if request.method == "GET":
        return Response(data={"message": "OK"}, status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        # message: str = request.data.get("text", "")
        return Response(data={"message": "OK"}, status=status.HTTP_200_OK)
    elif request.method == "DELETE" or request.method == "PATCH":
        # message: str = request.data.get("text", "")
        return Response(data={"message": "OK"}, status=status.HTTP_200_OK)


# TODO news ###########################################


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


@api_view(http_method_names=["GET", "POST"])  # DRF - django rest framework
def api(request: Request) -> Response:
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    # print(request.body)
    print(request.data)  # dictionary
    return Response(data={"message": "OK"}, status=status.HTTP_200_OK)


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

        message: str = request.data.get("message", "")
        with open("messages.txt", "a", encoding="utf-8") as file:
            file.write(f"{message}\n")

        return Response(data={"message": "OK"}, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE", "PATCH"])
def weather(request: Request) -> Response:
    if request.method == "GET":
        return Response(data={"text": "Сегодня отличная погода"}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # {"text": "Сегодня дождь!"}
        message: str = request.data.get("text", "")
        print(message)
        return Response(data={"message": "OK"}, status=status.HTTP_201_CREATED)


@api_view(http_method_names=["GET", "POST"])
def workers(request: Request) -> Response:
    if request.method == "GET":
        # TODO search

        def example():
            # Сериализация - превращение из Python -> JSON
            # 1. Сериализация (не для умных)
            # data = []
            # for i in workers_list:
            #     new_dict = {
            #         "id": i.id,
            #         "iin": i.iin,
            #         "first_name": i.first_name,
            #         "last_name": i.last_name,
            #     }
            #     data.append(new_dict)
            # return Response(data=data, status=status.HTTP_200_OK)
            # 2. Сериализация через DRF
            # users_obj = User.objects.all()
            # users_json = serializers.UserSerializer(users_obj, many=True).data
            # return Response(data=users_json, status=status.HTTP_200_OK)
            pass

        # http://127.0.0.1:8000/api/workers/?search=9708&sort_by=first_name
        # .order_by()
        workers_list = models.Worker.objects.filter(iin__icontains=request.query_params.get("search", ""))
        # workers_list = models.Worker.objects.all()  # возврат всех строк из базы данных
        data = serializers.WorkerSerializer(workers_list, many=True).data  # превращаем в json
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # откуда [HTTP]: api / pyqt6 / requests / frontend / html ...
        """
        {"iin": "9708777", "firstName": "Диас", "lastName": "Фамилия"}
        """
        # password = str(request.data.data['password'])
        # re.match("", "")
        # iin = str(request.data['iin']).strip()
        # TODO нужна валидация данных (проверка соответствия данных)

        new_worker = models.Worker.objects.create(
            iin=str(request.data["iin"]),  # unsafe - хочу ловить Exception если этого параметра нет,
            first_name=str(request.data.get("firstName", "")).strip(),  # safe
            last_name=str(request.data.get("lastName", "")).strip(),  # safe
        )
        # new_worker.delete()
        return Response(data={"message": "OK"}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={"message": "HTTP_405_METHOD_NOT_ALLOWED"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def workers_pk(request: Request, pk: str) -> Response:
    if request.method == "GET":
        # worker_obj = models.Worker.objects.get(id=int(pk))
        # worker_json = serializers.WorkerSerializer(worker_obj, many=False).data
        # return Response(data=worker_obj, status=status.HTTP_200_OK)
        return Response(data=serializers.WorkerSerializer(models.Worker.objects.get(id=int(pk)), many=False).data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        """
        /1 PUT - весь объект
        {"iin": "9708777", "firstName": "Диас", "lastName": "Фамилия"}

        /1 PATCH - частично
        {"firstName": "Диас3", "lastName": "Фамилия3"}"""
        worker_obj = models.Worker.objects.get(id=int(pk))

        iin = str(request.data.get("iin", ""))
        if len(iin) > 0:
            worker_obj.iin = iin

        first_name = str(request.data.get("firstName", ""))
        if len(first_name) > 0:
            worker_obj.first_name = first_name

        last_name = str(request.data.get("lastName", ""))
        if len(last_name) > 0:
            worker_obj.last_name = last_name

        worker_obj.save()

        return Response(data={"message": "successfully updated."}, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        models.Worker.objects.get(id=int(pk)).delete()
        return Response(data={"message": "successfully deleted."}, status=status.HTTP_200_OK)
    else:
        return Response(data={"message": "HTTP_405_METHOD_NOT_ALLOWED"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(http_method_names=["GET", "POST", "PUT", "DELETE"])
def rating(request: Request, post_id: str = "-1") -> Response:
    """
    Эй, фронтендер:

    {"user_id": 1354314, "value": 7, "post_id": 1354}

    """
    if request.method == "GET":
        # query_params(request.GET) = https://hh.ru/search/vacancy?text=Python&page=4
        # http://127.0.0.1:8000/api/rating/?post_id=12&value=7
        # search, page, limit...
        #
        # dynamic params () https://www.olx.kz/elektronika/telefony-i-aksesuary/
        # http://127.0.0.1:8000/api/rating/1
        # только для 1-2 параметров, обычно это всегда str/int и это первичные ключи
        # detail by 'id', category
        return Response(data={}, status=200)
    if request.method == "POST":
        #                                             danger
        # http://127.0.0.1:8000/api/rating/{post_id}/{user_id}/{value}
        #

        # http://127.0.0.1:8000/api/rating/1344?category=electro
        # {"user_id": 1354314, "value": 7}

        # html form  - <form><input type='text' name='text'/></form>
        print(request.GET)
        print(request.POST)  # default for multipart-form-data (django jinja)
        print(request.FILES)
        print(request.data)  # default for json data (django DRF)

        # post_id
        user_id = request.data.get("user_id", None)  # GO
        if user_id is None:
            raise Exception("user_id is None !")
        value = request.data["value"]  # unsafe == Exception
        _rating = models.Rating.objects.create(post_id=post_id, user_id=user_id, value=value)
        return Response(data={"id": str(_rating.id)}, status=status.HTTP_201_CREATED)


"""
SPA = выдавать наружу excel-файл.
SPA = выдавать на интерфейс html-таблицу.


"""


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def report(request: Request, point_id: str = "-1") -> Response:
    if point_id == "-1":
        if request.method == "GET":
            # todo Получение списка данных
            _ratings_obj = models.Rating.objects.all()
            _ratings_json = serializers.RatingSerializer(_ratings_obj, many=True).data
            return Response(data=_ratings_json, status=status.HTTP_200_OK)
        elif request.method == "POST":
            # Создание новой записи в базе данных
            return Response(data={"message": "success"}, status=status.HTTP_201_CREATED)
    else:
        if request.method == "GET":
            # Получение детальных данных по point_id
            return Response(data={"data": []}, status=status.HTTP_200_OK)
        elif request.method == "PUT":
            # Обновление записи по point_id
            return Response(data={"message": "success"}, status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            # Удаление записи по point_id
            return Response(data={"message": "success"}, status=status.HTTP_200_OK)