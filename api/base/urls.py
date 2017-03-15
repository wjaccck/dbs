# encoding: utf8

from rest_framework import routers
import views

# router = routers.DefaultRouter(trailing_slash=False)
router = routers.DefaultRouter()

router.register(r'ipv4address', views.Ipv4Address_ApiViewSet)
router.register(r'ipv4network', views.Ipv4Network_ApiViewSet)
router.register(r'status', views.Status_ApiViewSet)
router.register(r'machine_type', views.Machine_type_ApiViewSet)
router.register(r'role', views.Role_ApiViewSet)
router.register(r'environment', views.Environment_ApiViewSet)
router.register(r'idc', views.IDC_ApiViewSet)

urlpatterns = router.urls