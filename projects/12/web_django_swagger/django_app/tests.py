from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

# python manage.py test


class UserModelTestCase(TestCase):
    username = "Bogdan1"
    password = "Bogdan1!234fdr3f543"

    def setUp(self):  # преднастройка
        User.objects.create(username=self.username, password=make_password(self.password))

    def test_model_create(self):
        print("""Тестируем модель на корректное создание пользователя""")
        user = User.objects.get(username=self.username)
        self.assertEqual(user.username, self.username)


class NewsListTestCase(TestCase):
    def setUp(self):  # преднастройка
        pass

    def test_view(self):
        print("""Тестируем запрос к новостям""")
        client = Client()
        response = client.get(reverse("news"))
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SuccessfullTestCase(TestCase):
    def test(self):
        print(
            """\n\n\n
#################################\n
ALL TEST SUCCESSFULL\n
#################################\n
\n\n\n"""
        )
