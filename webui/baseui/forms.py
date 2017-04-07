# #coding=utf8
from django import forms
from api.base.models import *


class BaseForm(forms.ModelForm):

    name = forms.CharField(label='名称', max_length=255, widget=forms.TextInput({'class': 'form-control'}))

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



class StatusForm(BaseForm):

    class Meta:
        model = Status
        exclude = ['created_date', 'modified_date','creator','last_modified_by']


class Machine_typeForm(BaseForm):

    class Meta:
        model = Machine_type
        exclude = ['created_date', 'modified_date','creator','last_modified_by']


class RoleForm(BaseForm):

    class Meta:
        model = Role
        exclude = ['created_date', 'modified_date','creator','last_modified_by']


class EnvironmentForm(BaseForm):

    class Meta:
        model = Environment
        exclude = ['created_date', 'modified_date','creator','last_modified_by']

class IDCForm(BaseForm):

    class Meta:
        model = IDC
        exclude = ['created_date', 'modified_date', 'creator', 'last_modified_by']