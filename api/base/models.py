from __future__ import unicode_literals

from django.db import models

# Create your models here.
from abstract.models import UniqueNameDescModel,NameModel,CommonModel

class Ipv4Address(UniqueNameDescModel):

    class Meta:
        ordering = ['name', ]

class Ipv4Network(UniqueNameDescModel):
    gateway = models.CharField(max_length=18, null=True)

    class Meta:
        ordering = ['name', ]

class Status(NameModel):
    pass

class Machine_type(NameModel):
    pass

class Role(NameModel):
    pass

class Environment(NameModel):
    pass

class IDC(NameModel):
    pass

