from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="Наименование")
    description = models.TextField(max_length=3000, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        verbose_name="Изображение", upload_to="images/products", default=None, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        """Вспомогательный класс"""

        app_label = "django_app"
        ordering = ("-is_active", "title")
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title
