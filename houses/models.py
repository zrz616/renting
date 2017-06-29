# -*- coding:utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from Users.models import UserProfile


def address_validate(value):
    '''房源地址验证'''
    if value is None:
        raise ValidationError(
            "address can not be empty"
        )


class City(models.Model):
    """docstring for City"""
    city_name = models.CharField(max_length=20, verbose_name='城市名')

    class Meta(object):
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city_name


class School(models.Model):
    """学校信息"""
    school_name = models.CharField(max_length=20, verbose_name='附近学校名称')
    city = models.ForeignKey(City, default='', verbose_name='学校所在城市')

    class Meta(object):
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.school_name


class Device(models.Model):
    """设备"""
    device_id = models.SmallIntegerField(primary_key=True, default='')
    device_name = models.CharField(max_length=10, verbose_name='设备名')

    class Meta(object):
        verbose_name = '设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.device_name


# Create your models here.
class House(models.Model):
    """租房信息"""

    address = models.CharField(max_length=100, unique=True, validators=[address_validate], verbose_name='房源地址')
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='简介')
    detail = models.TextField(verbose_name='详情')
    landlord = models.ForeignKey(UserProfile, default='', verbose_name='房东')
    price = models.FloatField(verbose_name='出租价格')
    house_show = models.ImageField(upload_to='house/%Y/%m', verbose_name='房源展示')
    reservation = models.IntegerField(verbose_name='预约人数', default=0)
    favorite_nums = models.IntegerField(verbose_name='感兴趣的人数', default=0)
    house_type = models.CharField(max_length=20, verbose_name='户型')
    rent_choices = (
        ('whole', '整租'),
        ('share', '合租'),
    )
    rent_type = models.CharField(choices=rent_choices, default='whole', max_length=10)
    transport = models.CharField(max_length=50, verbose_name='交通状况')
    device = models.ManyToManyField(Device, null=True, blank=True, verbose_name='设施信息')
    school = models.ManyToManyField(School,
        through='Position',  # 指定中介表
        through_fields=('house', 'school'),
        verbose_name='周边学校'
    )

    class Meta(object):
        verbose_name = '房源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address


class Position(models.Model):
    """学校与公寓位置"""
    house = models.ForeignKey(House)
    school = models.ForeignKey(School)
    distance = models.IntegerField(verbose_name='住房到学校的距离')

    class Meta(object):
        ordering = ("distance",)
        verbose_name = '位置'
        verbose_name_plural = verbose_name
