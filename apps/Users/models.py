# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """扩展用户信息"""
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), default='female', max_length=10)
    number = models.CharField(max_length=11, verbose_name='手机')
    avatar = models.ImageField(upload_to="avatars/%Y/%m", default='avatars/default.png', max_length=100)

    class Meta(object):
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecode(models.Model):
    """记录邮箱验证码"""
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget_password', '忘记密码')), max_length=10)
    send_time = models.DateTimeField(default=datetime.now)
