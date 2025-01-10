# Generated by Django 5.1.4 on 2025-01-10 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myfirstapp", "0002_brand"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skills",
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
                ("skill_name", models.CharField(max_length=100)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("person_name", models.CharField(max_length=100)),
                ("skill", models.ManyToManyField(to="myfirstapp.skills")),
            ],
        ),
    ]
