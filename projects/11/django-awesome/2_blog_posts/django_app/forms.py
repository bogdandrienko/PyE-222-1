import datetime

from django import forms
from .models import Post


class PostForm(forms.ModelForm):  # cryspy-forms
    """Замена HTML форм"""

    time = forms.TimeField(
        disabled=False,  # Отключено ли поле в форме
        localize=False,  # Локализовать ли контент принудительно
        required=True,  # Требовать ли наличие данных в поле
        label="time",  # Заголовок поля
        help_text='<small class="text-muted underline">10:27</small><br>',  # Вспомогательный текст
        # для поля (Можно передавать html теги)
        initial=datetime.datetime.now().strftime("%H:%M"),  # Начальное значение поля (Имеет приоритет
        # перед "widget.attrs.value")
        widget=forms.TimeInput(
            attrs={
                "type": "time",  # HTML тип поля
                "name": "time",  # HTML имя поля
                "required": "",  # Требовать ли наличие данных в поле
                "placeholder": datetime.datetime.now().strftime("%H:%M"),  # Данные, которые видны при
                # удалении всей информации
                "value": datetime.datetime.now().strftime("%H:%M"),  # Начальное значение поля
                # (Второстепенное по приоритету после "initial")
                "class": "form-control",  # HTML / css / bootstrap классы
                "min": "01:00",
                "max": "22:59",
                "format": "%H:%M:%S",
            }
        ),
    )

    # + быстрее разработка, чем HTMl / встроенная валидация
    # - только для Jinja, сложно кастомизируемы
    class Meta:
        model = Post
        fields = "__all__"
        # fields = (
        #     "author",
        #     "title",
        #     "description",
        #     "image",
        #     "is_active",
        #     "date_time",
        # )
