from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator, FileExtensionValidator
from django.db import models


# Create your models here.
class Positions(models.Model):
    """
    Должность

    id

    Наименование
    ... (грейд, обязанности, права, уровени доступа...)

    """
    title = models.CharField(
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="-",
        verbose_name="Наименование должности",
        help_text='<small class="text-muted">уникальный</small><hr><br>',
        validators=[MinLengthValidator(1), MaxLengthValidator(300)],

        max_length=300,
    )

    class Meta:
        app_label = "django_documents"
        ordering = ("title", "id")
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return f"{self.title} ({self.id})"


class Moderators(models.Model):
    """
    Утверждающий

    id

    ФИО
    Должность
    """
    fio = models.CharField(
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="-",
        verbose_name="ФИО",
        help_text='<small class="text-muted">уникальный</small><hr><br>',
        validators=[MinLengthValidator(1), MaxLengthValidator(300)],

        max_length=300,
    )
    position = models.ForeignKey(
        verbose_name="Должность",
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',

        to=Positions,
        on_delete=models.CASCADE,  # CASCADE - каскадное удаление
        # on_delete=models.DO_NOTHING,  # DO_NOTHING - ничего не делать
        #
        # null=True,
        # on_delete=models.SET_NULL,  # SET_NULL - "занулить"
        #
        # default="something",
        # on_delete=models.SET_DEFAULT,  # SET_DEFAULT - установить в стандартное значение
    )

    class Meta:
        app_label = "django_documents"
        ordering = ("fio", "position", "id")
        verbose_name = "Модератор"
        verbose_name_plural = "Модераторы"

    def __str__(self):
        return f"{self.fio} ({self.id}) {self.position.title}"


class Categories(models.Model):
    """
    Категория

    id

    Заголовок
    Утверждающий
    """

    title = models.CharField(
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="-",
        verbose_name="Заголовок",
        help_text='<small class="text-muted">уникальный</small><hr><br>',
        validators=[MinLengthValidator(1), MaxLengthValidator(300)],

        max_length=300,
    )
    moderator = models.ForeignKey(
        verbose_name="Утверждающий",
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',

        to=Moderators,
        # on_delete=models.CASCADE,  # CASCADE - каскадное удаление
        # on_delete=models.DO_NOTHING,  # DO_NOTHING - ничего не делать
        #
        null=True,
        on_delete=models.SET_NULL,  # SET_NULL - "занулить"
        #
        # default="something",
        # on_delete=models.SET_DEFAULT,  # SET_DEFAULT - установить в стандартное значение
    )

    class Meta:
        app_label = "django_documents"
        ordering = ("title", "moderator", "id")
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.title} ({self.id}) {self.moderator.fio} [{self.moderator.position.title}]"


# class Documents(models.Model):
#     """
#     id
#
#     №
#     Заголовок
#     Краткое описание
#     Категория
#     файл
#
#     согласовал
#     утвердил
#
#     вступил ли в силу
#     устарел ли
#
#     дата
#     """
#     number = models.BigIntegerField(
#         unique=True,
#         editable=True,
#         blank=True,
#         null=False,
#         default=1,
#         verbose_name="Номер акта",
#         help_text='<small class="text-muted">от 1 до 999999999999</small><hr><br>',
#         validators=[MinValueValidator(1), MaxValueValidator(999999999999)]
#     )
#     title = models.CharField(
#         unique=True,
#         editable=True,
#         blank=True,
#         null=False,
#         default="-",
#         verbose_name="Заголовок",
#         help_text='<small class="text-muted">уникальный</small><hr><br>',
#         validators=[MinLengthValidator(1), MaxLengthValidator(300)],
#
#         max_length=300,
#     )
#     description = models.TextField(
#         unique=False,
#         editable=True,
#         blank=True,
#         null=False,
#         default="",
#         verbose_name="Заголовок",
#         help_text='<small class="text-muted"> до 9999</small><hr><br>',
#         validators=[MinLengthValidator(0), MaxLengthValidator(9999)],
#     )
#     category = models.ForeignKey()
#     addition = models.ForeignKey()
#
#     pass
