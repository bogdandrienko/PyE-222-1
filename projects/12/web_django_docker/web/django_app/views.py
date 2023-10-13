import random

from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    # cache
    value = cache.get("my_value")  # int | None
    if value is None:
        value = random.randint(1, 100000000)
        cache.set("my_value", value, 5)
    # cache

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

    return render(request, "Home.html", context={"value": value})
