# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0028_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='moviecode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='detail.Movie'),
        ),
    ]
