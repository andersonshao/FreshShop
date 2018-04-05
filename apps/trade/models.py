from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()

# Create your models here.


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, verbose_name='买家')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    nums = models.IntegerField(default=0, verbose_name='购买数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'goods')

    def __str__(self):
        return '%s(%d)' % (self.goods.name, self.nums)


class OrderInfo(models.Model):
    PAY_STATUS = (('success', '支付成功'), ('cancel', '取消'), ('wait', '待支付'))
    user = models.ForeignKey(User, verbose_name='买家')
    order_sn = models.CharField(max_length=50, verbose_name='订单号', unique=True, blank=True, null=True)
    trade_no = models.CharField(max_length=50, verbose_name='交易号')
    pay_status = models.CharField(choices=PAY_STATUS, default='wait', verbose_name='支付状态', max_length=10)
    post_script = models.CharField(max_length=100, verbose_name='备注', null=True, blank=True)
    total_price = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_sn


class OrderGoods(models.Model):
    order = models.ForeignKey(OrderInfo, verbose_name='订单')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    goods_num = models.IntegerField(default=0, verbose_name='商品数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn
