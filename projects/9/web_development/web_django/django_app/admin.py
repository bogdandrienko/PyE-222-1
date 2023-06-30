from django.contrib import admin
from django_app import models

admin.site.site_header = "Панель управления"  # default: "Django Administration"
admin.site.index_title = "Администрирование сайта"  # default: "Site administration"
admin.site.site_title = "Администрирование"  # default: "Django site admin"


class PostsAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Posts' на панели администратора
    """

    # список для отображения
    list_display = ("author", "title", "description", "date_time", "is_moderate")
    # список для перехода
    list_display_links = ("author", "title",)
    # для редактирования "в общем списке"
    list_editable = ("is_moderate",)
    # по каким полям нужна фильтрация
    list_filter = ("author", "title", "description", "date_time", "is_moderate")
    # как должен выглядеть детальный просмотр
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "author", "title", "description"
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
    # поиск по каким полям
    search_fields = ["title", "description"]


class PostsCommentsAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'PostsComments' на панели администратора
    """

    list_display = ("post_id", "author", "text", "date_time")
    list_display_links = ("post_id", "author", )
    list_editable = ()
    list_filter = ("post_id", "author", "text", "date_time")
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "post_id", "author", "text",
                )
            },
        ),
        (
            "Техническое",
            {
                "fields": (
                    "date_time",
                )
            },
        ),
    )
    search_fields = ["post_id", "author", "text"]


admin.site.register(models.Posts, PostsAdmin)  # complex
admin.site.register(models.PostComments, PostsCommentsAdmin)  # complex
admin.site.register(models.PostRatings)  # simple
