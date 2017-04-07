from django.conf.urls import include, url
import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    ###machine
    url(r'^machine/$',login_required(views.Machine_ListViewSet.as_view()),name='machine-list'),
    url(r'^machine/update/(?P<pk>\d+)/$',login_required(views.Machine_UpdateViewSet.as_view()),name='machine-update'),
    url(r'^machine/create/$',login_required(views.Machine_CreateViewSet.as_view()),name='machine-create'),

]
