# Generated by Django 2.2.16 on 2022-08-10 21:46

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220810_2126'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]