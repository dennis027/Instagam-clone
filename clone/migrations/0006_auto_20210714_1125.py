# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-07-14 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0005_auto_20210714_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
