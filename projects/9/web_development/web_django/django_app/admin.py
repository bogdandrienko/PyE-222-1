from django.contrib import admin
from django_app import models


admin.site.register(models.Posts)
admin.site.register(models.PostComments)
admin.site.register(models.PostRatings)
