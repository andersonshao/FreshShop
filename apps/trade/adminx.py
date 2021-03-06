from .models import ShoppingCart, OrderInfo, OrderGoods

import xadmin


class ShoppingCartAdmin(object):
    list_display = ['user', 'goods', 'nums', 'add_time']
    list_editable = list_display
    search_fields = ['user', 'goods']
    list_filter = list_display
    ordering = ['-nums']
    refresh_times = [3, 5]


class OrderInfoAdmin(object):
    list_display = ['user', 'order_sn', 'trade_no', 'pay_status', 'post_script', 'total_price', 'pay_time', 'add_time']
    list_editable = list_display
    search_fields = ['user', 'post_script']
    list_filter = list_display
    ordering = ['-pay_time']
    readonly_fields = ['order_sn', 'trade_no']


class OrderGoodsAdmin(object):
    list_display = ['order', 'goods', 'goods_num', 'add_time']
    search_fields = ['order', 'goods']
    list_filter = list_display


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderGoods, OrderGoodsAdmin)
