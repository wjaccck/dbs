#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from abstract.models import NameModel,CommonModel,BASE_FATHER

class Ipv4Address(NameModel):

    class Meta:
        ordering = ['name', ]

class Ipv4Network(NameModel):
    gateway = models.CharField(max_length=18, null=True)

    class Meta:
        ordering = ['name', ]

class Status(NameModel,BASE_FATHER):
    pass
    @staticmethod
    def verbose():
        return u'状态'

class Machine_type(NameModel,BASE_FATHER):
    pass
    @staticmethod
    def verbose():
        return u'服务器类型'

class Role(NameModel,BASE_FATHER):
    pass
    @staticmethod
    def verbose():
        return u'角色'


class Environment(NameModel,BASE_FATHER):
    pass
    @staticmethod
    def verbose():
        return u'环境'

class IDC(NameModel,BASE_FATHER):
    pass
    @staticmethod
    def verbose():
        return u'机房'

