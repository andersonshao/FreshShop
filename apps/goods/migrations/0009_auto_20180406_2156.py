# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20180406_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_num',
            field=models.IntegerField(default=100, verbose_name='库存'),
        ),
    ]
