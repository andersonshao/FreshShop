# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20180405_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='city',
            field=models.CharField(default='', max_length=100, verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='province',
            field=models.CharField(default='', max_length=100, verbose_name='省份'),
        ),
    ]
