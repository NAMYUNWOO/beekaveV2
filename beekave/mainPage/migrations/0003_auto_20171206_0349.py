# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_auto_20171205_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_rank_1',
            name='desc',
            field=models.CharField(default='Act', max_length=50),
        ),
        migrations.AlterField(
            model_name='movie_rank_2',
            name='desc',
            field=models.CharField(default='Story', max_length=50),
        ),
        migrations.AlterField(
            model_name='movie_rank_3',
            name='desc',
            field=models.CharField(default='Director', max_length=50),
        ),
        migrations.AlterField(
            model_name='movie_rank_4',
            name='desc',
            field=models.CharField(default='Ost', max_length=50),
        ),
        migrations.AlterField(
            model_name='movie_rank_5',
            name='desc',
            field=models.CharField(default='Visual', max_length=50),
        ),
        migrations.AlterField(
            model_name='movie_rank_6',
            name='desc',
            field=models.CharField(default='Fresh', max_length=50),
        ),
    ]