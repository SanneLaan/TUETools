# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 17:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tuetools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_current_course',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='document_file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='document',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]