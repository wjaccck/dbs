from __future__ import unicode_literals

from django.db import models
from abstract.models import CommonModel
from api.base.models import IDC,Environment,Role,Ipv4Address,Machine_type,Status
# Create your models here.

class Machine(CommonModel):
    cmdb_sn=models.CharField(max_length=50)
    sn=models.CharField(max_length=50)
    idc=models.ForeignKey(IDC,related_name='machine_idc')
    cpu=models.IntegerField()
    memory=models.IntegerField()
    disk_space=models.IntegerField()
    type=models.ForeignKey(Machine_type,related_name='machine_type')
    status=models.ForeignKey(Status,related_name='machine_status')

    class Meta:
        ordering = ['-created_date', ]

    def __unicode__(self):
        return self.cmdb_sn