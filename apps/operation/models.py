from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()

# Create your models here.


class UserFav(models.Model):
    user = models.ForeignKey(User, verbose_name='买家')
    goods = models.ForeignKey(Goods, verbose_name='商品')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserNotes(models.Model):
    MESSAGE_TYPE = (
        (1, '留言'),
        (2, '投诉'),
        (3, '询问'),
        (4, '售后'),
        (5, '求购')
    )
    user = models.ForeignKey(User, verbose_name='买家')
    message_type = models.IntegerField(verbose_name='留言类型', choices=MESSAGE_TYPE, default=1)
    subject = models.CharField(max_length=100, verbose_name='留言主题', default='')
    message = models.TextField(default='', verbose_name='留言内容', help_text='留言内容')
    file = models.FileField(verbose_name='上传文件', help_text='上传文件')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.subject


class UserAddress(models.Model):
    user = models.ForeignKey(User, verbose_name='买家')
    district = models.CharField(max_length=100, verbose_name='区域', default='')
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    signer_name = models.CharField(max_length=20, verbose_name='签收人', default='')
    signer_mobile = models.CharField(max_length=11, verbose_name='签收人电话', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.address
