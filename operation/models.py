# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models
from Users.models import UserProfile
from houses.models import House


class BaseRelationship(models.Model):

    user = models.ForeignKey(UserProfile, default='', related_name="%(app_label)s_%(class)s_related", verbose_name='用户')
    house = models.ForeignKey(House, default='', related_name="%(app_label)s_%(class)s_related", verbose_name='住房')

    class Meta:
        abstract = True


class UserFavorite(BaseRelationship):

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}用户收藏了{}'.format(self.user.username, self.house.address)


class Appointment(BaseRelationship):

    Appointment_id = models.SmallIntegerField(primary_key=True)
    appointment_time = models.DateTimeField(default=datetime.now, verbose_name='预约时间')

    class Meta:
        verbose_name = "预约"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.appointment_time)
