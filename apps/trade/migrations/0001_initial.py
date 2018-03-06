# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 06:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, verbose_name='商品数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(max_length=50, unique=True, verbose_name='订单号')),
                ('trade_no', models.CharField(max_length=50, verbose_name='交易号')),
                ('pay_status', models.CharField(choices=[('success', '支付成功'), ('cancel', '取消'), ('wait', '待支付')], default='wait', max_length=10, verbose_name='支付状态')),
                ('notes', models.CharField(max_length=100, verbose_name='备注')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='订单金额')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='支付时间')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, verbose_name='购买数量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
    ]
