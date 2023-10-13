# Generated by Django 4.2.5 on 2023-10-12 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0003_news"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ("-datetime_created",),
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
        migrations.AddField(
            model_name="news",
            name="datetime_created",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата публикации"
            ),
        ),
    ]
