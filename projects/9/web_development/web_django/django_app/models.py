from django.db import models
from django.utils import timezone


class Posts(models.Model):
    """
    CREATE TABLE IF NOT EXISTS posts
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author TEXT,
    title TEXT,
    description TEXT,
    datetime TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """

    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = "django_app"
        ordering = ("-date_time", "title")
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return f"{self.title} {self.date_time} {self.title}"


class PostComments(models.Model):
    """
    CREATE TABLE IF NOT EXISTS post_comments
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title_id INTEGER,
    author TEXT,
    text TEXT,
    datetime TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    """

    post_id = models.IntegerField()
    author = models.CharField(max_length=200)
    text = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = "django_app"
        ordering = ("-date_time", "post_id")
        verbose_name = "Комментарий к публикации"
        verbose_name_plural = "Комментарии к публикациям"

    def __str__(self):
        return f"{self.post_id} {self.date_time} {self.author}"


class PostRatings(models.Model):
    """
    CREATE TABLE IF NOT EXISTS post_ratings
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title_id INTEGER,
    rating INTEGER
    )
    """

    post_id = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        app_label = "django_app"
        ordering = ("-rating", "post_id")
        verbose_name = "Рейтинг к публикации"
        verbose_name_plural = "Рейтинги к публикациям"

    def __str__(self):
        return f"{self.post_id} {self.rating}"
