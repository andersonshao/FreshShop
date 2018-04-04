from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = ('user', 'goods')
        validators = [UniqueTogetherValidator(queryset=UserFav.objects.all(),
                                              fields=('user', 'goods'),
                                              message='已收藏')]

