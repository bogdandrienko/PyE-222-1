from django.contrib import admin
from django_app import models

admin.site.site_header = "Панель управления"  # default: "Django Administration"
admin.site.index_title = "Администрирование сайта"  # default: "Site administration"
admin.site.site_title = "Администрирование"  # default: "Django site admin"


class ProductAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Product' на панели администратора
    """

    list_display = ("title", "description", "price", "image", "is_active")
    list_display_links = (
        "title",
        "description",
    )
    list_editable = ("is_active",)
    list_filter = ("title", "description", "price", "image", "is_active")
    fieldsets = (
        (
            "Основное",
            {"fields": ("title", "description", "price", "image")},
        ),
        (
            "Техническое",
            {"fields": ("is_active",)},
        ),
    )
    search_fields = ["title", "description"]


# Register your models here.
admin.site.register(models.Product, ProductAdmin)
