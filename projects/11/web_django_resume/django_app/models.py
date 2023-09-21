from django.core import validators
from django.db import models


class Resume(models.Model):
    # фио, иин, дата рождения, место, образование, активно, пол
    first_name = models.CharField(max_length=300, validators=[validators.MinLengthValidator(5)])

    class Meta:
        app_label = 'django_app'
        ordering = ('-first_name',)
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        db_table = 'resume_model_table'

    def __str__(self):
        return f"<Resume {self.first_name}>"
