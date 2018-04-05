# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 14:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0004_auto_20180404_2013'),
        ('trade', '0002_auto_20180306_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='goods_num',
            new_name='nums',
        ),
        migrations.AlterUniqueTogether(
            name='shoppingcart',
            unique_together=set([('user', 'goods')]),
        ),
    ]
