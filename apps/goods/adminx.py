from .models import GoodsCategory, Goods, GoodsCategoryBrand, GoodsImage, Banner, IndexAd

import xadmin


class GoodsCategoryAdmin(object):
    list_display = ['id', 'name', 'code', 'desc', 'category_type', 'parent_category', 'is_tab', 'add_time']
    list_editable = list_display
    search_fields = ['name', 'desc']
    list_filter = ['code', 'desc', 'category_type', 'is_tab', 'add_time']
    ordering = ['-add_time']
    refresh_times = [3, 5]


class GoodsAdmin(object):
    list_display = ['name', 'category', 'click_num', 'ship_free', 'fav_num', 'is_hot', 'add_time']
    list_editable = list_display
    search_fields = ['name', 'goods_brief', 'goods_desc']
    list_filter = ['category',  'goods_brief', 'goods_desc', 'ship_free', 'is_new', 'is_hot', 'add_time']
    ordering = ['-click_num']
    readonly_fields = ['fav_num']
    model_icon = 'fa fa-bitbucket'
    refresh_times = [3, 5]
    style_fields = {'goods_desc': 'ueditor'}

    class GoodsImageInline(object):
        model = GoodsImage
        exclude = ['add_time']
        extra = 1
        style = 'tab'

    inlines = [GoodsImageInline]


class GoodsCategoryBrandAdmin(object):
    list_display = ['category', 'name', 'desc', 'image', 'add_time']
    search_fields = ['category', 'name', 'desc']
    list_filter = list_display

    def get_context(self):
        context = super(GoodsCategoryBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1, name__in=['酒水饮料', '粮油副食'])
        return context


# class GoodsImageAdmin(object):
#     list_display = ['goods', 'image', 'image_url', 'add_time']
#     search_fields = ['goods']
#     list_filter = list_display


class BannerAdmin(object):
    list_display = ['goods', 'image', 'index', 'add_time']
    search_fields = ['goods']
    list_filter = list_display


class IndexAdAdmin(object):
    list_display = ['goods', 'category']

    def get_context(self):
        context = super(IndexAdAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1, name__in=['酒水饮料', '粮油副食'])
            context['form'].fields['goods'].queryset = Goods.objects.filter()
        return context


xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsCategoryBrandAdmin)
# xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(IndexAd, IndexAdAdmin)
