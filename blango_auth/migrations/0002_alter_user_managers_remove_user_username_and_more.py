# Generated by Django 4.1.7 on 2023-03-29 18:00

import blango_auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blango_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", blango_auth.models.BlangoUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
