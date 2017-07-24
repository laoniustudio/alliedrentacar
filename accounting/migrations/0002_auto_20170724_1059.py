# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allimage',
            name='mainImg',
            field=models.ImageField(default='ss', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('ONRENT', 'On Rent'), ('REVIEW', 'Ready for review'), ('PASS', 'Pass'), ('FAIL', 'Fail')], default='REVIEW', max_length=50),
        ),
    ]
