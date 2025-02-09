# Generated by Django 5.1.5 on 2025-01-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_news_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("O", "Other"),
                            ("P", "Prefer not to say"),
                        ],
                        max_length=1,
                    ),
                ),
                ("is_adult", models.BooleanField(default=False)),
            ],
        ),
    ]
