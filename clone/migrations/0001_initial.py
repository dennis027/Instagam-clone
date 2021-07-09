# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-07-09 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='MEDIA/')),
                ('caption', models.CharField(max_length=30)),
                ('Comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.Comments')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Profile_photo', models.ImageField(upload_to='MEDIA/')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='Likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.Likes'),
        ),
        migrations.AddField(
            model_name='image',
            name='Profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.Profile'),
        ),
    ]
