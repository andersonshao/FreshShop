from random import choice

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.yunpian import YunPian
from FreshShop.settings import API_KEY
from .models import VerifyCode
from .serializers import SmsSerializers, UserRegSerializer, UserDetailSerializer


User = get_user_model()


# Create your views here.


class CustomBackends(ModelBackend):
    """
    自定义用户验证规则
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SmsSerializers

    def generate_code(self):
        seeds = '1234567890'
        l = []
        for _ in range(4):
            l.append(choice(seeds))
        return ''.join(l)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']

        code = self.generate_code()

        yun_pian = YunPian(API_KEY)
        result = yun_pian.send_sms(code, mobile)

        if result['code'] != 0:
            return Response({
                'mobile': result['msg']
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            verify_code = VerifyCode(code=code, mobile=mobile)
            verify_code.save()
            return Response({
                'mobile': mobile
            }, status=status.HTTP_201_CREATED)


class UserViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def get_object(self):
        return self.request.user

    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsAuthenticated()]
        elif self.action == 'create':
            return []
        return []

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegSerializer
        return UserDetailSerializer
