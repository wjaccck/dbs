# #coding=utf8
from django import forms
from api.resource_pool.models import Resource_pool
from webui.wiget import *


class BaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.creator = kwargs.pop('creator', None)
        self.last_modified_by = kwargs.pop('last_modified_by', None)
        super(BaseForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(BaseForm, self).save(commit=False)
        if self.creator:
            instance.creator = self.creator
        if self.creator:
            instance.last_modified_by = self.last_modified_by
        return instance.save()



class Resource_poolForm(BaseForm):
    os = forms.CharField(label='系统', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    cpu = forms.CharField(label='CPU', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    memory = forms.CharField(label='内存', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    disk_space = forms.CharField(label='磁盘', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    swap = forms.CharField(label='swap', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    class Meta:
        model = Resource_pool

        fields = (
            'machine',
            'm_ip',
            'ips',
            'role',
            'os',
            'cpu',
            'memory',
            'disk_space',
            'swap',
            'status',
        )
        widgets = {
                    'machine': MachineModelSelect2Widget,
                    'm_ip': IpModelSelect2Widget,
                    'ips': IpsModelSelect2MultipleWidget,
                    'role': RoleModelSelect2Widget,
                    'status': StatusModelSelect2Widget,
        }
        exclude = ['created_date', 'modified_date','creator','last_modified_by']

