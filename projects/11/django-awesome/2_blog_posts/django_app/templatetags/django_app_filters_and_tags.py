from django import template
import datetime
from django.contrib.auth.models import User, Group
from django.http import HttpRequest

from django_app import models

# Фильтры и тэги (jinja)
# Для изменения отображения данных в шаблоне, для логики внутри шаблонов

# 0. strftime
# 1. Смена округления
# 2. Сменить запятую на точку, и наоборот (разные языки)
# 3. Формат с разделителями (раздение числа при слишком больших значениях)
# 4. Нужно написать тэг, который проверяет группы у пользователя


register = template.Library()


@register.simple_tag(takes_context=True)
def check_user_group(context: str, groups: str = "", cnt=1, c=1) -> bool:
    try:
        user: User = context["request"].user

        # print(groups)       # "Модераторы контента, Модераторы, Модераторы, Привет"
        groups_list = sorted(list(set([x.strip() for x in groups.split(",")])), reverse=False)
        # print(groups_list)  # ['Модераторы', 'Модераторы контента', 'Привет']

        this_user_groups: list[str] = [x.name for x in user.groups.all()]
        # print(this_user_groups)  # ['Модераторы контента', 'Основатели']

        for i in this_user_groups:  # линейная
            # for j in groups_list:     # квадратичная
            #     if i == j:
            #         return True
            if i in groups_list:
                return True
        return False
    except Exception as error:
        print("error simple_tag check_user_group: ", error)
        return False


@register.simple_tag()
def digit_beautify(value):
    print("value: ", value)

    src = str(value)

    out, rnd = src.split(".")
    print(f"out: {out}")
    # TODO костыль
    if 3 < len(out) <= 6:
        out = out[3:] + " " + out[0:3]
    elif 6 < len(out) <= 9:
        out = out[6:] + " " + out[3:6] + " " + out[0:3]
    elif 9 < len(out) <= 12:
        out = out[9:] + " " + out[6:9] + " " + out[3:6] + " " + out[0:3]
    elif 12 < len(out) <= 15:
        out = out[12:] + " " + out[9:12] + " " + out[6:9] + " " + out[3:6] + " " + out[0:3]
    return f"{out},{rnd}"  # out = out.replace(".", ",")  # TODO русификация разрядов


@register.simple_tag(takes_context=True)
def text_upper_case(context: str, text: str):
    try:
        return str(text).upper() + " kokos"
    except Exception as error:
        print("error simple_tag text_upper_case: ", error)
        return ""


@register.filter(name="format_datetime")
def format_datetime(source: datetime.datetime, format: str = ""):  # SIMPLE TAG
    """Преобразует дату в строку в формате datetime"""

    # , tz_hours: float = 6.0
    # source = source + datetime.timedelta(hours=tz_hours)

    match format:  # match-case (switch-case - js/go) - хэширует(запоминает) значения своих кейсов
        case "time":
            return source.strftime("%H:%M:%S")
        case "time1":
            return source.strftime("%H-%M-%S")
        case "date":
            return source.strftime("%d.%m.%Y")
        case "date2":
            return source.strftime("%d.%m.%Y") + "banana"
        case _:
            return source


@register.filter(name="rounding")
def rounding(source: float | int, count_len: int = 0):
    """Округление дробных значений"""
    # try:
    if count_len < 0:
        raise ValueError(f"ERROR count_len = {count_len}")
    elif count_len == 0:
        return int(source)
    else:
        return round(source, count_len)
    # except Exception as e:
    #     print(e)
    #     return source


@register.filter(name="my_slice")
def my_slice(source: str, length: int):
    """"""

    return source[:length]


@register.simple_tag(takes_context=True)
def check_user_access(context: str, groups: str = "") -> bool:
    try:
        user: User = context["request"].user
        group_objs = user.groups.all()
        group_strs = [str(x.name).lower().strip() for x in group_objs]
        if str(groups).lower().strip() in group_strs:
            return True
        return False
    except Exception as error:
        print("error simple_tag check_user_access: ", error)
        return False


@register.simple_tag(takes_context=True)
def i_liked_this_post(context: str, post_pk: str) -> int:
    try:
        request: HttpRequest = context["request"]
        post = models.Post.objects.get(id=int(post_pk))

        ratings = models.PostRatings.objects.filter(post=post, author=request.user)
        if len(ratings) < 1:
            return 0
        else:
            rating = ratings[0]
            if rating.status:
                return 1
            return -1
    except Exception as error:
        print("error simple_tag i_liked_this_post: ", error)
        return 0


@register.simple_tag(takes_context=True)
def user_groups(context: dict) -> list:
    try:
        request: HttpRequest = context["request"]
        user = request.user
        if user.is_anonymous:
            return []
        names = []
        for i in user.groups.all():
            names.append(i.name)
        return names
    except:
        return []
