# from django.shortcuts import redirect
# from django.views.generic.base import View

from rest_framework import serializers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from .models import UserProfile, EmailVerifyRecode
from .forms import RegisterForm


class AccountSerializers(serializers.Serializer):
    """
        在注册用户或更新邮箱密码时使用
    """
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirmed_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['confirmed_password']:
            raise serializers.ValidationError("passwords not match")
        data.pop('confirmed_password')
        return data

    def create(self, validate_data):
        print('create')
        # 使用create创建的密码是明文,
        # 而create_user会产生用默认加密方式加密的密码
        # return UserProfile.objects.create(**validate_data)
        return UserProfile.objects.create_user(**validate_data)

    def update(self, instance, validated_data):
        print("update")
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        password = validated_data.get('password', None)
        instance.make_password(password)
        instance.save()

        return instance


class UserProfileSerializers(serializers.ModelSerializer):
    """
        ModelSerializer 不支持非model字段只写
        创建用户要使用到confirmed_password字段
        所以这里只在用户资料表时用来查询用户信息
    """
    class Meta:
        """
            @param: model 指定序列化的对象
            @param: field 指定序列化的字段, 值为一个元组或'__all__'
            @param: depth 指定序列化的深度，为1说明字段下一层进行序列化
        """
        model = UserProfile
        fields = ('email', 'username', 'nick_name', 'avatar', 'gender')
        read_only_fields = ('email', 'username')  # 用户名和邮箱不允许随意修改
        # TODO


class EmailVerifySerializers(serializers.ModelSerializer):

    class Meta:
        model = EmailVerifyRecode
        fields = '__all__'


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def login_status(request):
    if request.user.is_authenticated:
        body = {'msg': 'Successful', 'status': True, 'username': request.user.username}
        return Response(body, status=status.HTTP_200_OK)
    else:
        body = {'msg': 'Auth fail', 'status': False}
        return Response(body, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def flush_captcha(request):
    if request.method == 'GET':
        new_captcha = dict()
        new_captcha['key'] = CaptchaStore.generate_key()
        new_captcha['image'] = captcha_image_url(new_captcha['key'])
        return Response(new_captcha, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_account(request):
    if request.method == 'POST':
        # print(request.POST)
        # 对输入的合法性及验证码校验
        register_form = RegisterForm(request.POST)
        # print('errors')
        # print(register_form.errors.as_data())
        if register_form.is_valid():
            serializer = AccountSerializers(data=request.data)
            if serializer.is_valid():
                print(serializer.validated_data)
                # UserProfile.objects.create_user(**serializer.validated_data)
                serializer.save()
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            return Response({
                            'status': 'Bad request',
                            'message': 'les données ne sont pas valides'
                            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({'invaild': 'Form error'}, status=status.HTTP_400_BAD_REQUEST)
