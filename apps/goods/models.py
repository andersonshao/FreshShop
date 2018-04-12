from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1, '一级类'),
        (2, '二级类'),
        (3, '三级类')
    )
    name = models.CharField(max_length=20, default='', verbose_name='类别名', help_text='类别名')
    code = models.CharField(max_length=30, default='', verbose_name='类别code', help_text='类别code')
    desc = models.TextField(default='', verbose_name='类别描述', help_text='类别描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='类别', help_text='类别')
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name='父类', help_text='父类', related_name='sub_cat')
    is_tab = models.BooleanField(default=False, verbose_name='是否导航', help_text='是否导航')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类别', null=True, blank=True, related_name='brands')
    name = models.CharField(max_length=30, default='', verbose_name='品牌名', help_text='品牌名')
    desc = models.TextField(default='', verbose_name='品牌描述', help_text='品牌描述')
    image = models.ImageField(upload_to='brands/images', verbose_name='品牌图片', max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类别')
    goods_sn = models.CharField(max_length=50, verbose_name='商品唯一货号', default='')
    name = models.CharField(max_length=50, verbose_name='商品名')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    sold_num = models.IntegerField(default=0, verbose_name='销售量')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    goods_num = models.IntegerField(default=100, verbose_name='库存')
    market_price = models.FloatField(default=0.0, verbose_name='市价')
    shop_price = models.FloatField(default=0.0, verbose_name='本店价格')
    goods_brief = models.CharField(max_length=500, default='', verbose_name='商品简述')
    goods_desc = UEditorField(verbose_name='内容', imagePath='goods/images', width=1000, height=300, filePath='goods/file', default='')
    goods_front_image = models.ImageField(verbose_name='封面', upload_to='goods/images', default='')
    ship_free = models.BooleanField(verbose_name='是否免邮', default=False)
    is_new = models.BooleanField(verbose_name='是否新品', default=False)
    is_hot = models.BooleanField(verbose_name='是否热销', default=False)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, verbose_name='商品', related_name='images')
    image = models.ImageField(upload_to='', verbose_name='图片', max_length=200, null=True, blank=True)
    image_url = models.CharField(max_length=200, verbose_name='图片url', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Goods, verbose_name='商品')
    image = models.ImageField(upload_to='banners', verbose_name='图片', max_length=200)
    index = models.IntegerField(default=0, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类别', related_name='category', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '首页广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWord(models.Model):
    keywords = models.CharField(max_length=10, verbose_name='热搜词', null=True, blank=True)
    index = models.IntegerField(default=0, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
