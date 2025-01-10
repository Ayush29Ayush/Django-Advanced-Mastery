# Generated by Django 5.1.4 on 2025-01-10 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myfirstapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("brand_name", models.CharField(max_length=100)),
                ("country", models.CharField(default="IN", max_length=100)),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["brand_name", "country"],
                        name="myfirstapp__brand_n_a4e772_idx",
                    )
                ],
                "unique_together": {("brand_name", "country")},
            },
        ),
    ]