#coding=utf8
from django.db.models import Q
from api.machine.models import Machine
from django.core.urlresolvers import reverse_lazy
import forms
import operator
from abstract.views import Base_CreateViewSet,Base_ListViewSet,Base_UpdateViewSet



class Machine_CreateViewSet(Base_CreateViewSet):
    model = Machine
    form_class = forms.MachineForm
    template_name = 'api/assets/machine_form.html'
    success_url = reverse_lazy('machine-list')

class Machine_UpdateViewSet(Base_UpdateViewSet):
    model = Machine
    form_class = forms.MachineForm
    template_name = 'api/assets/machine_form.html'
    success_url = reverse_lazy('machine-list')

class Machine_ListViewSet(Base_ListViewSet):
    Machine.objects.all().count()
    model = Machine
    template_name = 'api/assets/machine.html'
    paginate_by = 10

    def get_queryset(self):
        name=None
        try:
            name=self.request.GET['keyword']
        except:
            pass

        if name:
            return Machine.objects.select_related().filter(cmdb_sn__icontains=name)
        else:
            return Machine.objects.select_related().all()