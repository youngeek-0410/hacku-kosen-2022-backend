# Generated by Django 4.1.4 on 2022-12-16 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_alter_project_spotify_uri_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="spotify_uri",
            field=models.CharField(
                default="spotify:album:6uqewERWZ1vzfCcin1zFIp", max_length=256
            ),
        ),
    ]
