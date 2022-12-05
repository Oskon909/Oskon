# Generated by Django 4.1.3 on 2022-12-05 16:55

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
                ("title", models.CharField(max_length=50, verbose_name="Category")),
                ("icon_image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Food",
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
                ("date_create", models.DateTimeField(auto_created=True)),
                ("title", models.CharField(max_length=50, verbose_name="Food")),
                (
                    "description",
                    models.TextField(max_length=500, verbose_name="Description"),
                ),
                ("price", models.IntegerField(verbose_name="Price")),
                ("icon_image", models.ImageField(upload_to="")),
            ],
        ),
    ]
