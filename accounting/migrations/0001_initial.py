# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoreImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboardImg', models.ImageField(upload_to='')),
                ('frontImg', models.ImageField(upload_to='')),
                ('passFrontImg', models.ImageField(upload_to='')),
                ('passRearImg', models.ImageField(upload_to='')),
                ('rearImg', models.ImageField(upload_to='')),
                ('driveRear', models.ImageField(upload_to='')),
                ('driveFront', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='moreimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Post'),
        ),
    ]