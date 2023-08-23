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


admin.site.register(models.Product, ProductAdmin)


class CompaintAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Product' на панели администратора
    """

    list_display = ("username", "text", "type", "is_active", "date_time")
    list_display_links = ("username", "text", "type")
    list_editable = ("is_active",)
    list_filter = ("username", "text", "type", "is_active", "date_time")
    fieldsets = (
        (
            "Основное",
            {"fields": ("username", "text", "type")},
        ),
        (
            "Техническое",
            {
                "fields": (
                    "is_active",
                    "date_time",
                )
            },
        ),
    )
    search_fields = ["username", "text", "type"]


admin.site.register(models.Complaint, CompaintAdmin)


class CitiesAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Cities' на панели администратора
    """

    list_display = ("name", "index", "type", "is_active")
    list_display_links = ("name", "index")
    list_editable = (
        "type",
        "is_active",
    )
    list_filter = ("name", "index", "type", "is_active")
    fieldsets = (
        (
            "Основное",
            {"fields": ("name", "index")},
        ),
        (
            "Техническое",
            {"fields": ("type", "is_active")},
        ),
    )
    search_fields = ["name", "index"]


admin.site.register(models.Cities, CitiesAdmin)
