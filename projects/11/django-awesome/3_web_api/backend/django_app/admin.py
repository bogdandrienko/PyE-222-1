from django.contrib import admin
from django_app import models


# class WorkerAdmin(admin.ModelAdmin):
#     list_display = ("author", "title", "description", "image", "is_active", "date_time")
#     list_display_links = (
#         "author",
#         "title",
#         "description",
#     )
#     list_editable = ("is_active",)
#     list_filter = ("author", "title", "description", "image", "is_active", "date_time")
#     fieldsets = (
#         (
#             "Основное",
#             {"fields": ("author", "title", "description", "image")},
#         ),
#         (
#             "Техническое",
#             {"fields": ("is_active", "date_time")},
#         ),
#     )
#     search_fields = ["title", "description"]
#
#
# admin.site.register(models.Worker, WorkerAdmin)
admin.site.register(models.Worker)
admin.site.register(models.Rating)
