# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-29 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import tableau.models


class Migration(migrations.Migration):

    dependencies = [
        ('tableau', '0003_auto_20160327_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='post',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=tableau.models.upload_location),
        ),
    ]