from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav, UserNotes, UserAddress
from goods.serializers import GoodsSerializer


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        fields = ('user', 'goods', )
        validators = [UniqueTogetherValidator(queryset=UserFav.objects.all(),
                                              fields=('user', 'goods'),
                                              message='已收藏')]


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ('goods', 'id')


class UserNotesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserNotes
        fields = '__all__'


class UserAddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    signer_name = serializers.CharField(required=True)
    signer_mobile = serializers.CharField(required=True)

    class Meta:
        model = UserAddress
        fields = '__all__'
