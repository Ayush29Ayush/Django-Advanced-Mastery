# Generated by Django 5.1.5 on 2025-01-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageModel",
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
                ("original_image", models.ImageField(upload_to="images/")),
                (
                    "thumbnail_mini",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/thumbnails"
                    ),
                ),
                (
                    "thumbnail_small",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/thumbnails"
                    ),
                ),
                (
                    "thumbnail_medium",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/thumbnails"
                    ),
                ),
                (
                    "thumbnail_large",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/thumbnails"
                    ),
                ),
            ],
        ),
    ]
