import random
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
import threading
from django_app import tasks as django_app_celery
from django_settings.celery import app as current_celery_app
from celery.result import AsyncResult


# Create your views here.

def home(request):
    if request.method == "POST":
        def log():
            """
            Плюс:
            * Задача в фоновом режиме

            Минусы:
            * Нагрузка, т.е. нельзя задачу делать в нужный
            * Планировщик - отсутвует функционал планировщика задач
            * Результат - нет отчёта о работе
            * Есть риск, что поток "упадёт" не отработав
            """
            requests.post(
                "http://127.0.0.1:8000/api/logger",
                json={"text": request.POST["text"], "count": 666, "is_hide": False}
            )

        threading.Thread(target=log).start()
    return render(request, "Home.html")


def books(request):
    data = requests.get("http://127.0.0.1:8000/home").json()
    return JsonResponse(data)


def celer(request):
    # bulk_mail
    # for i in messages
    """
    Для улучшения пользовательского опыта, продолжительные процессы должны
    выполняться в фоновом режиме вне обычного потока HTTP-запросов/ответов.
    Например:

    Отправка писем для подтверждения;
    Парсинг;
    Анализ данных;
    Обработка изображений;
    Генерация отчетов.

    При создании приложения, старайтесь отделять задачи, которые должны выполняться в
    течение жизненного цикла запроса/ответа, например CRUD-операции, от задач, которые
    должны выполняться в фоновом режиме.
    """

    """
    # ssh
    sudo apt-get update -y
    sudo apt-get install -y openssh-server
    sudo systemctl start ssh
    sudo systemctl restart ssh
    ip a
    # ssh
    
    # redis
    sudo apt update -y
    sudo apt install -y redis
    redis-server
    redis-cli
    ping # PONG
    exit
    # redis
    
    
    # python
    python3.11 -V
    sudo apt-get update -y
    sudo apt-get install -y wget
    sudo apt-get install -y build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get install -y python3.11 python3.11-venv python3.11-dev
    python3.11 -V
    # python
    
    # web
    cd ~/Downloads/web
    python3.11 -m venv env
    source env/bin/activate
    python -V
    pip install celery django-redis
    pip install -r requirements.txt
    python manage.py runserver 0.0.0.0:8000
    http://127.0.0.1:8000/celer/
    # web
    
    # celery
    python -m celery -A django_settings worker -l info
    # celery
    
    """

    #

    # task_id = django_app_celery.add(random.randint(1, 10), random.randint(1, 10))  # прямой вызов
    # task_id = django_app_celery.add.apply_async((random.randint(1, 10), random.randint(1, 10)))  # *ARGS
    # print(task_id)
    #
    # # c6f55087-2769-4df4-8945-244693faa416

    # TODO GET RESULT FROM CELERY
    task_id = "ed8a9aa0-6cee-4b89-8161-be55560c66fa"
    result = AsyncResult(task_id, app=current_celery_app)
    if result.state == "SUCCESS":
        res = f"{result.state} {result.get()}"
    else:
        res = f"{result.state} {None}"

    # 1 init
    # 2 send
    # 3 in progress(STARTED)
    # 4 completed(SUCCESS)
    # 5 failed

    # task_id = django_app_celery.send_mass_mail.apply_async()  # **KWARGS
    # print(task_id)
    # # # первый запрос - начинаем рассылку сотни писем
    # res = ""

    # task_id = ""
    # res = django_app_celery.send_mass_mail()

    return HttpResponse(f"<h1>Task_id: {task_id} [{res}]</h1>")


def start(request):
    # TODO START CELERY TASK
    task_id = django_app_celery.send_mass_mail.apply_async()
    return HttpResponse(f"<h1>Task_id: {task_id}</h1>")
