# from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserFavSerializer, UserFavDetailSerializer, UserNotesSerializer, UserAddressSerializer
from .models import UserFav, UserNotes, UserAddress
from utils.permissions import IsOwnerOrReadOnly

# Create your views here.


class UserFavViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    serializer_class = UserFavSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = 'goods_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavDetailSerializer
        if self.action == 'create':
            return UserFavSerializer
        return UserFavSerializer

    def perform_destroy(self, instance):
        goods = instance.goods
        goods.fav_num -= 1
        goods.save()
        instance.delete()


class UserNotesViewSet(viewsets.ModelViewSet):
    serializer_class = UserNotesSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserNotes.objects.filter(user=self.request.user)


class UserAddressViewSet(viewsets.ModelViewSet):
    serializer_class = UserAddressSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
