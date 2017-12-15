# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_rank_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('movieCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_rank_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('movieCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_rank_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('movieCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_rank_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('movieCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_rank_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('movieCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_rank_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(unique=True)),
                ('movieCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Movie')),
            ],
        ),
    ]