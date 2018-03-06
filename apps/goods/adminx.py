from .models import GoodsCategory, Goods, GoodsCategoryBrand, GoodsImage, Banner

import xadmin


class GoodsCategoryAdmin(object):
    list_display = ['name', 'code', 'desc', 'category_type', 'parent_category', 'is_tab', 'add_time']
    list_editable = list_display
    search_fields = ['name', 'desc', 'category_type', 'parent_category']
    list_filter = ['code', 'desc', 'category_type', 'is_tab', 'add_time']
    ordering = ['-add_time']
    refresh_times = [3, 5]


class GoodsAdmin(object):
    list_display = ['category', 'goods_sn', 'name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price', 'shop_price', 'goods_brief', 'goods_desc', 'cover', 'ship_free', 'is_new', 'is_hot', 'add_time']
    list_editable = list_display
    search_fields = ['category', 'goods_sn', 'name', 'goods_brief', 'goods_desc']
    list_filter = ['goods_sn', 'name', 'click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price', 'shop_price', 'goods_brief', 'goods_desc', 'ship_free', 'is_new', 'is_hot', 'add_time']
    ordering = ['-click_num']
    readonly_fields = ['fav_num']
    model_icon = 'fa fa-bitbucket'
    refresh_times = [3, 5]
    style_fields = {'goods_desc': 'ueditor'}


class GoodsCategoryBrandAdmin(object):
    list_display = ['category', 'name', 'desc', 'image', 'add_time']
    search_fields = ['category', 'name', 'desc']
    list_filter = list_display


class GoodsImageAdmin(object):
    list_display = ['goods', 'image', 'image_url', 'add_time']
    search_fields = ['goods']
    list_filter = list_display


class BannerAdmin(object):
    list_display = ['goods', 'image', 'index', 'add_time']
    search_fields = ['goods']
    list_filter = list_display


xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)
