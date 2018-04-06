"""FreshShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_view
from rest_framework_jwt.views import obtain_jwt_token
import xadmin

from FreshShop.settings import MEDIA_ROOT
from goods import views as goods_views
from users import views as users_views
from operation import views as operation_views
from trade import views as trade_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'goods', goods_views.GoodsViewSet, base_name='goods')
router.register(r'categories', goods_views.CategoryViewSet, base_name='categories')
router.register(r'codes', users_views.SmsCodeViewSet, base_name='codes')
router.register(r'users', users_views.UserViewSet, base_name='users')
router.register(r'userfavs', operation_views.UserFavViewSet, base_name='userfavs')
router.register(r'messages', operation_views.UserNotesViewSet, base_name='messages')
router.register(r'address', operation_views.UserAddressViewSet, base_name='address')
router.register(r'shopcarts', trade_views.ShoppingCartViewSet, base_name='shopcarts')
router.register(r'orders', trade_views.OrderViewSet, base_name='orders')
router.register(r'banners', goods_views.BannerViewSet, base_name='banners')
router.register(r'indexgoods', goods_views.IndexCategoryViewSet, base_name='indexgoods')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^robots.txt/$', TemplateView.as_view(template_name='robots.txt'), name='robots'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', token_view.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),
    url(r'^docs/', include_docs_urls(title='ANDERSON生鲜超市')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

]
