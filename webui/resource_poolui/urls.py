from django.conf.urls import include, url
import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    ### resource
    url(r'^pool/$',login_required(views.Resource_pool_ListViewSet.as_view()),name='resource-pool-list'),
    url(r'^pool/update/(?P<pk>\d+)/$',login_required(views.Resource_pool_UpdateViewSet.as_view()),name='resource-pool-update'),
    url(r'^pool/create/$',login_required(views.Resource_pool_CreateViewSet.as_view()),name='resource-pool-create'),

]
