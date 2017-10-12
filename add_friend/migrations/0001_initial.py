# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=27)),
                ('url', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
