from django.contrib import admin
from django_app import models

admin.site.site_header = "Панель управления"  # default: "Django Administration"
admin.site.index_title = "Администрирование сайта"  # default: "Site administration"
admin.site.site_title = "Администрирование"  # default: "Django site admin"


class PostAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Post' на панели администратора
    """

    list_display = ("author", "title", "description", "image", "is_active", "date_time")
    list_display_links = (
        "author",
        "title",
        "description",
    )
    list_editable = ("is_active",)
    list_filter = ("author", "title", "description", "image", "is_active", "date_time")
    fieldsets = (
        (
            "Основное",
            {"fields": ("author", "title", "description", "image")},
        ),
        (
            "Техническое",
            {"fields": ("is_active", "date_time")},
        ),
    )
    search_fields = ["title", "description"]


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.PostComments)
admin.site.register(models.PostRatings)
