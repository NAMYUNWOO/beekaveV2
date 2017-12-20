# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0027_auto_20171219_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.URLField(null=True)),
                ('moviecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
            ],
        ),
    ]
