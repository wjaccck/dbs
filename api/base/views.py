# encoding: utf8

from django.db.models import Count
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from .models import *
from .serializers import *
# from rest_framework_filters.backends import DjangoFilterBackend


class Base_ApiViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    # Allow methods
    http_method_names = ['get']
    queryset=Ipv4Address.objects.select_related('creator', 'last_modified_by')\
                                .all()
    serializer_class = IPv4AddressSerializer
    # Applies permissions
    permission_classes = (permissions.DjangoModelPermissions,)
    # Applies Filters
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields = ('name',)
    search_fields = ('^name', )

    def perform_create(self, serializer):
        serializer.save(
            creator = self.request.user,
            last_modified_by = self.request.user
        )
        return super(Base_ApiViewSet, self).perform_create(serializer)

class Ipv4Address_ApiViewSet(Base_ApiViewSet):
    # Allow methods
    http_method_names = ['get']
    queryset=Ipv4Address.objects.select_related('creator', 'last_modified_by')\
                                .all()
    serializer_class = IPv4AddressSerializer


class Ipv4Network_ApiViewSet(Base_ApiViewSet):
    # Allow methods
    http_method_names = ['get', 'post']
    queryset=Ipv4Network.objects.select_related('creator', 'last_modified_by')\
                                .all()
    serializer_class = IPv4NetworkSerializer

class Status_ApiViewSet(viewsets.ModelViewSet):
    # Allow methods
    http_method_names = ['get', 'post']
    queryset=Status.objects.all()
    serializer_class = StatusSerializer

class Machine_type_ApiViewSet(viewsets.ModelViewSet):
    # Allow methods
    http_method_names = ['get', 'post']
    queryset=Machine_type.objects.all()
    serializer_class = Machine_typeSerializer


class Role_ApiViewSet(viewsets.ModelViewSet):
    # Allow methods
    http_method_names = ['get', 'post']
    queryset=Role.objects.all()
    serializer_class = RoleSerializer


class Environment_ApiViewSet(viewsets.ModelViewSet):
    # Allow methods
    http_method_names = ['get', 'post']
    queryset=Environment.objects.all()
    serializer_class = EnvironmentSerializer

class IDC_ApiViewSet(viewsets.ModelViewSet):
    # Allow methods
    http_method_names = ['get', 'post']

    queryset=Environment.objects.all()
    serializer_class = EnvironmentSerializer