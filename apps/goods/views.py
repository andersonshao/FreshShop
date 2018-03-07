from rest_framework import viewsets

from .models import Goods
from .serializers import GoodsSerializer


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Goods.objects.order_by('id')
    serializer_class = GoodsSerializer
