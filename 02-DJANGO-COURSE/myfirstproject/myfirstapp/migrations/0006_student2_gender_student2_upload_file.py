# Generated by Django 5.1.4 on 2025-01-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myfirstapp", "0005_alter_student_date_of_birth"),
    ]

    operations = [
        migrations.AddField(
            model_name="student2",
            name="gender",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="student2",
            name="upload_file",
            field=models.FileField(blank=True, null=True, upload_to="files/"),
        ),
    ]