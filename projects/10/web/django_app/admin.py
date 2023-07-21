from django.contrib import admin
from django_app import models

admin.site.site_header = "Панель управления"  # default: "Django Administration"
admin.site.index_title = "Администрирование сайта"  # default: "Site administration"
admin.site.site_title = "Администрирование"  # default: "Django site admin"


class MemAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Mem' на панели администратора
    """

    list_display = ("author", "title", "description", "image", "date_time", "is_moderate")
    list_display_links = ("author", "title",)
    list_editable = ("is_moderate",)
    list_filter = ("author", "title", "description", "image", "date_time", "is_moderate")
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "author", "title", "description", "image",
                )
            },
        ),
        (
            "Техническое",
            {
                "fields": (
                    "date_time", "is_moderate"
                )
            },
        ),
    )
    search_fields = ["title", "description"]

class NewsAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'News' на панели администратора
    """

    list_display = ("author", "title", "description", "image", "date_time", "is_ban")
    list_display_links = ("author", "title",)
    list_editable = ("is_ban",)
    list_filter = ("author", "title", "description", "image", "date_time", "is_ban")
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "author", "title", "description", "image",
                )
            },
        ),
        (
            "Техническое",
            {
                "fields": (
                    "date_time", "is_ban"
                )
            },
        ),
    )
    search_fields = ["title", "description"]


admin.site.register(models.Mem, MemAdmin)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.NewsComments)
admin.site.register(models.NewsRatings)
