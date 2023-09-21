# Generated by Django 4.2.5 on 2023-09-21 15:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=300,
                        validators=[django.core.validators.MinLengthValidator(5)],
                    ),
                ),
            ],
            options={
                "verbose_name": "Резюме",
                "verbose_name_plural": "Резюме",
                "db_table": "resume_model_table",
                "ordering": ("-first_name",),
            },
        ),
    ]