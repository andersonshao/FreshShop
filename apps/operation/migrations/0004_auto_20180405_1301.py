# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20180404_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotes',
            name='file',
            field=models.FileField(help_text='上传文件', upload_to='notes/images/', verbose_name='上传文件'),
        ),
    ]
