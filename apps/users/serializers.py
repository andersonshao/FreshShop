import re
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from FreshShop.settings import REGX_MOBILE
from .models import VerifyCode

User = get_user_model()


class SmsSerializers(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已存在')

        if not re.match(REGX_MOBILE, mobile):
            raise serializers.ValidationError('手机号非法')

        one_minute_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minute_age):
            raise serializers.ValidationError('距离上次发送不超过60s')

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(min_length=4, max_length=4, required=True,
                                 label='验证码', write_only=True,
                                 error_messages={
                                     'blank': '验证码为空',
                                     'min_length': '验证码格式错误',
                                     'max_length': '验证码格式错误',
                                 })
    username = serializers.CharField(required=True, allow_blank=False, validators=[UniqueValidator(queryset=User.objects.all(), message='用户已存在')], label='用户名')
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label='密码')

    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data)
    #     user.set_passoword(validated_data['password'])
    #     user.save()
    #     return user

    def validate_code(self, code):
        verify_codes = VerifyCode.objects.filter(mobile=self.initial_data['username'], code=code).order_by('-add_time')
        if verify_codes:
            last_record = verify_codes[0]
            five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if last_record.code != code:
                raise serializers.ValidationError('验证码错误')
            elif last_record.add_time < five_minute_ago:
                raise serializers.ValidationError('验证码过期')
        else:
            raise serializers.ValidationError('验证码不存在')

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ('mobile', 'username', 'code', 'password')
