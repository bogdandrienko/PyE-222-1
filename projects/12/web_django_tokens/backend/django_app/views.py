from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

"""
Есть данные, которые нельзя видеть/менять/удалять... всем подряд.

* Новости на главной странице(список). - они общедоступны. [auth(аутентификация) - нет, role(авторизация) - нет]
* Публикация новости. - только зарегистированным пользователям. [auth - да, role(авторизация) - нет]
* Редактирование профиля. - и админ и сам пользователь. [auth - да, role(авторизация) - да]
* Список всех пользователей системы(с личными данными). - они строго по определённому уровню доступа. [auth - да, role - да]

Аутентификация - "залогиниться", т.е. войти под своим аккаунтом.
Авторизация - "определить уровень доступа", т.е. понять может ли этот пользователь делать это действие.

session_id - Токен аутентификации.

user
stZCnidT6fypVj_

Active
Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
- если отключить, в систему нельзя аутентифицироваться.

Staff status
Designates whether the user can log into this admin site.
- позволяет входить в админ часть сайта

Superuser status
Designates that this user has all permissions without explicitly assigning them.
- даёт все права

#################################################

session_id - Django MVT (не подходит для api)

Django DRF - REST-api
API - программный интерфейс(общение двух программ). JSON -> JSON

- если чужая система не умеет сохранять в кукесы session_id,
этой системе придёт в КАЖДОМ запросе присылать логин и пароль.

* JWT-token:
* Фронтендер присылает Вам логин и пароль.
* Создать токен и послать в чужую систему. И следующие 10(N) минут, запросы которые идут с этим токеном,
* мы считаем, что они от этого пользователя.

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NzgxMTkxMywiaWF0IjoxNjk3NzI1NTEzLCJqdGkiOiI3N2VkMGJjYmJjM2E0Yzc0OGE2MTM4NDczMzE0NTA2NCIsInVzZXJfaWQiOjJ9.giR_jtqJBSFJJ2j5klHrqtvgUygQbLFSiR7IeTmITN4",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3NzI1ODEzLCJpYXQiOjE2OTc3MjU1MTMsImp0aSI6IjcyOWM4ZmE1MWFkMzRmNDlhOGYwYzc1MzZlNzkwZTJlIiwidXNlcl9pZCI6Mn0.RGEGt9XJKyxWfY0qkG4gk9yY0QMbood4BDFTL9-PwxY"
}

{
    "refresh": - одноразовый токен для обновления токенов
    "access": - токен доступа, его будет фронтендер присылать каждый раз внутри headers
} 

"""


def get_users():
    users = User.objects.all()
    user_json = []
    for i in users:
        user_json.append({"id": i.id, "username": i.username, "email": i.email, "password": i.password})
    return user_json


def public_users_list(request):
    _users = get_users()
    return JsonResponse(data={"message": "OK", "list": _users}, safe=False)


@login_required(login_url="login")  # встроенный в Django - перенаправляет на страницу логина
def private_users_list(request):
    # if not request.user.is_authenticated:  # custom - самодельный, т.е. можно логику реализовать самому
    #     raise Exception("Not authenticated")
    _users = get_users()
    return JsonResponse(data={"message": "OK", "list": _users}, safe=False)


@login_required(login_url="login")
def admin_users_list(request):
    if not request.user.is_superuser:
        raise Exception("You are not superuser!")
    _users = get_users()
    return JsonResponse(data={"message": "OK", "list": _users}, safe=False)


@login_required(login_url="login")
def our_moderator_users_list(request):
    current_user = request.user

    target_group = Group.objects.get(name="Наши модераторы")
    has = current_user.groups.filter(name=target_group.name).count()
    if has <= 0:
        raise Exception("Вы не наш модератор!")

    _users = get_users()
    return JsonResponse(data={"message": "OK", "list": _users}, safe=False)


def f_login(request):
    if request.method == "GET":
        # человек просто перешёл по ссылке или его перенаправил @login_required
        return render(request, "login.html")
    elif request.method == "POST":
        # получение формы от пользователя
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise Exception("Логин или пароль неверные!")
        login(request, user)  # сохрание session_id в кукесы(cookies), локальное хранилище браузера
        return redirect(reverse('private_users_list'))


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  # 1 ур - всем
def drf_public_users_list(request):
    _users = get_users()
    return Response(data={"message": "OK", "list": _users}, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])  # 2 ур - всем, кто аутентифицирован
def drf_private_users_list(request):
    _users = get_users()
    return Response(data={"message": "OK", "list": _users}, status=status.HTTP_200_OK)


def f_logout(request):
    logout(request)  # удаляет session_id
    return redirect(reverse('login'))
