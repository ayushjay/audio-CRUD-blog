# Generated by Django 5.0.1 on 2024-01-25 04:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_audio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="audio",
            field=models.FileField(upload_to="media/songdir"),
        ),
    ]
