# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-14 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0015_auto_20171215_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='audit',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='nation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='opendate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='showtime',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='titleen',
            field=models.CharField(max_length=200, null=True),
        ),
    ]