# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 12:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detail', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('comment', models.CharField(max_length=2000)),
                ('score', models.FloatField()),
                ('recommend', models.IntegerField()),
                ('nonRecommend', models.IntegerField()),
                ('movieCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
                ('reviewUser', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('votingUser', models.ManyToManyField(related_name='votingUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
