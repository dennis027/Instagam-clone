# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-07-11 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='image',
            old_name='Comments',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='Likes',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='Profile',
            new_name='profile',
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=tinymce.models.HTMLField(default=13.5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='poster',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
