import time

from rest_framework import serializers

from .models import ShoppingCart, OrderInfo, OrderGoods
from goods.models import Goods
from goods.serializers import GoodsSerializer


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nums = serializers.IntegerField(label='数量', error_messages={'required': '请选择购买数量', 'min_num': '商品数量不能小于1'})
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        nums = self.validated_data['nums']
        goods = self.validated_data['goods']

        exsited = ShoppingCart.objects.filter(user=user, goods=goods)

        if exsited:
            exsited = exsited[0]
            exsited.nums += nums
            exsited.save()
        else:
            exsited = ShoppingCart.objects.create(**validated_data)

        return exsited

    def update(self, instance, validated_data):
        instance.nums = self.validated_data['nums']
        instance.save()
        return instance


class ShoppingCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pay_status = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'

    def generate_order_sn(self):
        from random import Random
        random_ins = Random()
        order_sn = '{time_str}{userid}{ranstr}'.format(time_str=time.strftime('%Y%m%d%H%M%S'), userid=self.context['request'].user.id, ranstr=random_ins.randint(10, 99))
        return order_sn

    def validate(self, attrs):
        attrs['order_sn'] = self.generate_order_sn()
        return attrs


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'
