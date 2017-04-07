from django.conf.urls import include, url
import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    ###status
    url(r'^status/$',login_required(views.Status_ListViewSet.as_view()),name='status-list'),
    url(r'^status/update/(?P<pk>\d+)/$',login_required(views.Status_UpdateViewSet.as_view()),name='status-update'),
    url(r'^status/create/$',login_required(views.Status_CreateViewSet.as_view()),name='status-create'),

    ###machine_type
    url(r'^machine-type/$', login_required(views.Machine_type_ListViewSet.as_view()), name='machine-type-list'),
    url(r'^machine-type/update/(?P<pk>\d+)/$', login_required(views.Machine_type_UpdateViewSet.as_view()), name='machine-type-update'),
    url(r'^machine-type/create/$', login_required(views.Machine_type_CreateViewSet.as_view()), name='machine-type-create'),

    ###role
    url(r'^role/$', login_required(views.Role_ListViewSet.as_view()), name='role-list'),
    url(r'^role/update/(?P<pk>\d+)/$', login_required(views.Role_UpdateViewSet.as_view()),name='role-update'),
    url(r'^role/create/$', login_required(views.Role_CreateViewSet.as_view()),name='role-create'),

    ###environment
    url(r'^environment/$', login_required(views.Environment_ListViewSet.as_view()), name='environment-list'),
    url(r'^environment/update/(?P<pk>\d+)/$', login_required(views.Environment_UpdateViewSet.as_view()), name='environment-update'),
    url(r'^environment/create/$', login_required(views.Environment_CreateViewSet.as_view()), name='environment-create'),

    ###idc
    url(r'^idc/$', login_required(views.IDC_ListViewSet.as_view()), name='idc-list'),
    url(r'^idc/update/(?P<pk>\d+)/$', login_required(views.IDC_UpdateViewSet.as_view()),
        name='idc-update'),
    url(r'^idc/create/$', login_required(views.IDC_CreateViewSet.as_view()), name='idc-create'),

]
