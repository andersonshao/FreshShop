from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Goods
from .serializers import GoodsSerializer
from .filters import GoodsFilter


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    商品列表页，过滤、搜索、排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ['name', 'goods_brief', 'goods_desc']
    ordering_fields = ['click_num', 'sold_num', 'fav_num', 'goods_num', 'market_price', 'shop_price', 'add_time']
    ordering = ('-goods_num', )
