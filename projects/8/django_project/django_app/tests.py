import re

from django.test import TestCase


# Create your tests here.
def test(email):
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise Exception(f"Ошибка ввода почты {email}")
    print("success")


test("bogdandrienko@gmail.com")
test("dina1@gmail.com")
test("dina.1@com")
