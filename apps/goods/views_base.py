from django.views.generic import View
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import Goods

# Create your views here.


class GoodsListView(View):
    def get(self, request):
        goods = Goods.objects.all()[:10]
        json_data = serialize('json', goods)
        return HttpResponse(json_data, content_type='application/json')
