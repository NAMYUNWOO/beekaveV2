# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0002_auto_20171205_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='accessUrl',
        ),
    ]