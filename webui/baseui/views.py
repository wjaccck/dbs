#coding=utf8
from django.db.models import Q
from api.base.models import Status,Machine_type,Role,IDC,Environment
from django.core.urlresolvers import reverse_lazy
import forms
import operator
from abstract.views import Base_CreateViewSet,Base_ListViewSet,Base_UpdateViewSet



class Status_CreateViewSet(Base_CreateViewSet):
    model = Status
    form_class = forms.StatusForm
    template_name = 'api/base/status_form.html'
    success_url = reverse_lazy('status-list')

class Status_UpdateViewSet(Base_UpdateViewSet):
    model = Status
    form_class = forms.StatusForm
    template_name = 'api/base/status_form.html'
    success_url = reverse_lazy('status-list')

class Status_ListViewSet(Base_ListViewSet):
    Status.objects.all().count()
    model = Status
    template_name = 'api/base/status.html'
    paginate_by = 10

    def get_queryset(self):
        name=None
        try:
            name=self.request.GET['keyword']
        except:
            pass

        if name:
            return Status.objects.filter(name__icontains=name)
        else:
            return Status.objects.all()

class Machine_type_CreateViewSet(Base_CreateViewSet):
    model = Machine_type
    form_class = forms.Machine_typeForm
    template_name = 'api/base/machine_type_form.html'
    success_url = reverse_lazy('machine-type-list')
    
class Machine_type_UpdateViewSet(Base_UpdateViewSet):
    model = Machine_type
    form_class = forms.Machine_typeForm
    template_name = 'api/base/machine_type_form.html'
    success_url = reverse_lazy('machine-type-list')

class Machine_type_ListViewSet(Base_ListViewSet):
    Machine_type.objects.all().count()
    model = Machine_type
    template_name = 'api/base/machine_type.html'
    paginate_by = 10

    def get_queryset(self):
        name=None
        try:
            name=self.request.GET['keyword']
        except:
            pass

        if name:
            return Machine_type.objects.filter(name__icontains=name)
        else:
            return Machine_type.objects.all()


class Role_CreateViewSet(Base_CreateViewSet):
    model = Role
    form_class = forms.RoleForm
    template_name = 'api/base/role_form.html'
    success_url = reverse_lazy('role-list')

class Role_UpdateViewSet(Base_UpdateViewSet):
    model = Role
    form_class = forms.RoleForm
    template_name = 'api/base/role_form.html'
    success_url = reverse_lazy('role-list')

class Role_ListViewSet(Base_ListViewSet):
    Role.objects.all().count()
    model = Role
    template_name = 'api/base/role.html'
    paginate_by = 10

    def get_queryset(self):
        name=None
        try:
            name=self.request.GET['keyword']
        except:
            pass

        if name:
            return Role.objects.filter(name__icontains=name)
        else:
            return Role.objects.all()


class Environment_CreateViewSet(Base_CreateViewSet):
    model = Environment
    form_class = forms.EnvironmentForm
    template_name = 'api/base/environment_form.html'
    success_url = reverse_lazy('environment-list')

class Environment_UpdateViewSet(Base_UpdateViewSet):
    model = Environment
    form_class = forms.EnvironmentForm
    template_name = 'api/base/environment_form.html'
    success_url = reverse_lazy('environment-list')

class Environment_ListViewSet(Base_ListViewSet):
    Environment.objects.all().count()
    model = Environment
    template_name = 'api/base/environment.html'
    paginate_by = 10

    def get_queryset(self):
        name=None
        try:
            name=self.request.GET['keyword']
        except:
            pass

        if name:
            return Environment.objects.filter(name__icontains=name)
        else:
            return Environment.objects.all()


class IDC_CreateViewSet(Base_CreateViewSet):
    model = IDC
    form_class = forms.IDCForm
    template_name = 'api/base/idc_form.html'
    success_url = reverse_lazy('idc-list')

class IDC_UpdateViewSet(Base_UpdateViewSet):
    model = IDC
    form_class = forms.IDCForm
    template_name = 'api/base/idc_form.html'
    success_url = reverse_lazy('idc-list')

class IDC_ListViewSet(Base_ListViewSet):
    IDC.objects.all().count()
    model = IDC
    template_name = 'api/base/idc.html'
    paginate_by = 10

    def get_queryset(self):
        name=None
        try:
            name=self.request.GET['keyword']
        except:
            pass

        if name:
            return IDC.objects.filter(name__icontains=name)
        else:
            return IDC.objects.all()