# Generated by Django 5.0.4 on 2024-04-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category", models.CharField(max_length=20, verbose_name="Категория")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="FinData",
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
                ("date", models.DateField(verbose_name="Дата операции")),
                ("value", models.FloatField(max_length=10, verbose_name="Сумма")),
                (
                    "operation",
                    models.CharField(
                        default="Расход", max_length=10, verbose_name="Операция"
                    ),
                ),
                ("category", models.CharField(max_length=20, verbose_name="Категория")),
            ],
            options={
                "verbose_name": "Фин данные",
                "verbose_name_plural": "Фин данные",
            },
        ),
    ]
