import random
from time import timezone

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django.utils.timezone import now

"""
Расширение модели пользователя(добавление чего-то, аватарка)

1. "Вмешаться" в модель пользователя --
+ простота
- удаление или обновление env невозможны

2. "Отнаследоваться" от модели пользователя
+ Модель единая, т.е. одна
- можно задеть "стандартное" поведение и "сломать" логику остальных модулей

3. Создать вспомогательной модели
+ безопасность
- 2 модели

"""


class UserProfile(models.Model):
    """
    Модель, которая содержит расширение для стандартной модели пользователя веб-платформы
    """

    user = models.OneToOneField(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name="Модель пользователя",
        help_text='<small class="text-muted">Тут лежит "ссылка" на модель пользователя</small><hr><br>',
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",  # user.profile
    )
    avatar = models.ImageField(verbose_name="Аватарка", upload_to="users/avatars", default=None, null=True, blank=True)

    class Meta:
        """Вспомогательный класс"""

        app_label = "auth"
        ordering = ("-user", "avatar")
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return f"<UserProfile {self.user.username}>"


@receiver(post_save, sender=User)
def create_user_model(sender, instance, created, **kwargs):
    UserProfile.objects.get_or_create(user=instance)
    # created - за булево значение, "создана ли модель"
    # if created:
    #     UserProfile.objects.get_or_create(user=instance)


class Post(models.Model):
    """Наша модель поста"""

    author = models.ForeignKey(verbose_name="Автор", to=User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", upload_to="images/products", default=None, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активность поста", default=True)
    date_time = models.DateTimeField(default=now, verbose_name="Дата и время подачи")

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-is_active", "title")
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"<Post {self.title} {self.author.username}>"


class PostComments(models.Model):
    """Комментарии к постам"""

    post = models.ForeignKey(to=Post, verbose_name="К какому посту", max_length=200, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, verbose_name="Автор", max_length=200, on_delete=models.CASCADE)  # +-
    text = models.TextField("Текст комментария", default="")
    date_time = models.DateTimeField("Дата и время создания", default=now)

    class Meta:
        app_label = "django_app"
        ordering = ("-date_time", "post")
        verbose_name = "Комментарий к посту"
        verbose_name_plural = "Комментарии к постам"

    def __str__(self):
        return f"{self.date_time} {self.author.username} {self.post.title} {self.text[:20]}"


class PostRatings(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)  # OneToMany +-
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        app_label = "django_app"
        ordering = ("-post", "author")
        verbose_name = "Рейтинг к новости"
        verbose_name_plural = "Рейтинги к новостям"

    def __str__(self):
        if self.status:
            like = "ЛАЙК"
        else:
            like = "ДИЗЛАЙК"
        return f"{self.post.title} {self.author.username} {like}"


class UserAuthToken(models.Model):
    user = models.ForeignKey(verbose_name="Пользователь", to=User, on_delete=models.CASCADE)
    token = models.CharField(verbose_name="Токен", max_length=300)
    # можно добавить время создания и не пускать позже 3 дней
    # можно добавить одноразовое использование
    # ...

    class Meta:
        app_label = "django_app"
        ordering = ("-user", "token")
        verbose_name = "Токен доступа"
        verbose_name_plural = "Токены доступа"

    def __str__(self):
        return f"{self.user.username} {self.token}"

    @staticmethod
    def token_generator() -> str:
        def generate_track(length: int, characters: str) -> str:
            return "".join(random.choice(characters) for _ in range(length))

        f1 = "NL"
        f2 = generate_track(4, "1234567890")
        f3 = generate_track(4, "1234567890")
        f4 = generate_track(3, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # f1  f2   f3   f4
        # NL13541342KJG
        return f"{f1}{f2}{f3}{f4}"
