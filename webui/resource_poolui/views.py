#coding=utf8
from django.db.models import Q
from api.resource_pool.models import Resource_pool
from django.core.urlresolvers import reverse_lazy
import forms
import operator
from abstract.views import Base_CreateViewSet,Base_ListViewSet,Base_UpdateViewSet



class Resource_pool_CreateViewSet(Base_CreateViewSet):
    model = Resource_pool
    form_class = forms.Resource_poolForm
    template_name = 'api/resource/pool_form.html'
    success_url = reverse_lazy('resource-pool-list')

class Resource_pool_UpdateViewSet(Base_UpdateViewSet):
    model = Resource_pool
    form_class = forms.Resource_poolForm
    template_name = 'api/resource/pool_form.html'
    success_url = reverse_lazy('resource-pool-list')

class Resource_pool_ListViewSet(Base_ListViewSet):
    Resource_pool.objects.all().count()
    model = Resource_pool
    template_name = 'api/resource/pool.html'
    paginate_by = 10

    def get_queryset(self):
        host=None
        try:
            host=self.request.GET['keyword']
        except:
            pass

        if host:
            return Resource_pool.objects.select_related().filter(cmdb_sn__icontains=host)
        else:
            return Resource_pool.objects.select_related().all()