#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel,RESOURCE_BASE
from api.base.models import IDC,Environment,Role,Ipv4Address,Machine_type,Status
from api.machine.models import Machine
# Create your models here.

class Resource_pool(CommonModel,RESOURCE_BASE):
    machine=models.ForeignKey(Machine)
    ips=models.ManyToManyField(Ipv4Address,related_name='resource_ip')
    m_ip=models.ForeignKey(Ipv4Address,related_name='resource_mip')
    os=models.CharField(max_length=50)
    cpu=models.IntegerField()
    memory=models.IntegerField()
    disk_space=models.IntegerField()
    swap=models.IntegerField(default=0)
    role=models.ForeignKey(Role,related_name='resource_role')
    status=models.ForeignKey(Status,related_name='role_status')

    class Meta:
        ordering = ['-created_date', ]

    def __unicode__(self):
        return self.m_ip.name

    @staticmethod
    def verbose():
        return u'可用资源'