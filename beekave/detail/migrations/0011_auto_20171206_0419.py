# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0010_auto_20171206_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='audits',
            new_name='audit',
        ),
    ]
