from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"Book {self.title} ({self.id})"
