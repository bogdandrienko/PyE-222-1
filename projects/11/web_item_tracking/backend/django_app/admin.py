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


class ItemAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Item' на панели администратора
    """

    list_display = ("track", "status", "target", "weight", "width", "height", "depth", "contact", "address", "price", "is_active", "date_time_start")
    list_display_links = ("track", "target", "contact", "address")
    list_editable = ("status", "is_active")
    list_filter = ("track", "status", "target", "weight", "width", "height", "depth", "contact", "address", "price", "is_active", "date_time_start")
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "track",
                    "target",
                    "contact",
                    "address",
                    "price",
                )
            },
        ),
        (
            "Характеристики",
            {
                "fields": (
                    "weight",
                    "width",
                    "height",
                    "depth",
                )
            },
        ),
        (
            "Техническое",
            {
                "fields": (
                    "status",
                    "is_active",
                    "date_time_start",
                )
            },
        ),
    )
    search_fields = ["track", "contact", "address"]


admin.site.register(models.Item, ItemAdmin)


class FindAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Find' на панели администратора
    """

    list_display = ("user",)
    list_display_links = ("user",)
    list_editable = ()
    list_filter = ("user", "tracks")
    filter_horizontal = ("tracks",)
    fieldsets = (
        (
            "Основное",
            {"fields": ("user",)},
        ),
        (
            "Основное 2",
            {"fields": ("tracks",)},
        ),
    )
    search_fields = ["user", "tracks"]


admin.site.register(models.Find, FindAdmin)
admin.site.register(models.IceCreamType)
admin.site.register(models.IceCream)
admin.site.register(models.BookCategory)


class BookAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    list_editable = ()
    list_filter = ("name", "category")
    filter_horizontal = ("category",)
    fieldsets = (
        (
            "Основное",
            {"fields": ("name",)},
        ),
        (
            "Основное 2",
            {"fields": ("category",)},
        ),
    )
    search_fields = ["name", "category"]


admin.site.register(models.Book, BookAdmin)
