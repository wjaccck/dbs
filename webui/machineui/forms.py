# #coding=utf8
from django import forms
from api.machine.models import Machine
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



class MachineForm(BaseForm):
    cmdb_sn = forms.CharField(label='资产编号', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    sn = forms.CharField(label='SN', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    cpu = forms.CharField(label='CPU', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    memory = forms.CharField(label='内存', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    disk_space = forms.CharField(label='磁盘', max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    class Meta:
        model = Machine

        fields = (
            'cmdb_sn',
            'sn',
            'cpu',
            'memory',
            'disk_space',
            'idc',
            'type',
            'status',
        )
        widgets = {
                    'idc': IDCModelSelect2Widget,
                    'type': Machine_typeModelSelect2Widget,
                    'status': StatusModelSelect2Widget,
                }
        exclude = ['created_date', 'modified_date','creator','last_modified_by']

