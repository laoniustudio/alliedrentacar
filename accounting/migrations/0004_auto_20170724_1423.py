# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_auto_20170724_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateInTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
