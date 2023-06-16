from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="-",
        verbose_name="Автор",
        help_text='<small class="text-muted">автор поста</small><hr><br>',
        #
        max_length=200,
    )
    title = models.CharField(
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default="-",
        verbose_name="Заголовок поста",
        help_text='<small class="text-muted"></small><hr><br>',
        #
        max_length=200,
    )
    text = models.TextField(
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default="-",
        verbose_name="Описание поста",
        help_text='<small class="text-muted"></small><hr><br>',
    )
    datetime = models.DateTimeField(
        verbose_name="Дата и время создания",
        help_text='<small class="text-muted">время создания поста</small><hr><br>',
        default=timezone.now,
    )

    class Meta:
        app_label = "forum"
        ordering = ("-datetime", "title")
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return f"{self.title} {self.datetime}"
