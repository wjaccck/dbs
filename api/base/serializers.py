# encoding: utf8
from rest_framework import serializers
from netaddr import *
from abstract.serializers import CommonHyperlinkedModelSerializer,NameHyperlinkedModelSerializer
from api.base.models import Ipv4Address, Ipv4Network, Status, Machine_type, Role, Environment, IDC


class IPv4AddressSerializer(CommonHyperlinkedModelSerializer):

    class Meta:
        fields = '__all__'
        model = Ipv4Address

class IPv4NetworkSerializer(CommonHyperlinkedModelSerializer): 


    class Meta:
        fields = '__all__'
        model = Ipv4Network

    def create(self, validated_data):
        prefix = validated_data['name']
        nwk = IPNetwork(prefix)        
        rawAddrs = [Ipv4Address(name=str(x), creator=validated_data['creator'], \
                    last_modified_by=validated_data['last_modified_by']) for x in list(nwk)]
        addresses = Ipv4Address.objects.bulk_create(rawAddrs, batch_size=30)
        return super(IPv4NetworkSerializer, self).create(validated_data)

    def validate(self, attrs):
        if attrs['name'].find('/') == -1:
            raise serializers.ValidationError('Network mask is missing!')

        return super(IPv4NetworkSerializer, self).validate(attrs)

class StatusSerializer(CommonHyperlinkedModelSerializer):
        class Meta:
            fields = '__all__'
            model = Status

class Machine_typeSerializer(CommonHyperlinkedModelSerializer):
        class Meta:
            fields = '__all__'
            model = Machine_type

class RoleSerializer(CommonHyperlinkedModelSerializer):
        class Meta:
            fields = '__all__'
            model = Role

class EnvironmentSerializer(CommonHyperlinkedModelSerializer):
        class Meta:
            fields = '__all__'
            model = Environment

class IDCSerializer(CommonHyperlinkedModelSerializer):
        class Meta:
            fields = '__all__'
            model = IDC

# class Item_listserializers(serializers.ModelSerializer):
#     item = serializers.StringRelatedField()
#     app = serializers.StringRelatedField()
#     tech = serializers.StringRelatedField()
#     front = serializers.StringRelatedField(many=True)
#     app_link = serializers.StringRelatedField(many=True)
#     mysql_link = serializers.StringRelatedField(many=True)
#     redis_link = serializers.StringRelatedField(many=True)
#     codis_link = serializers.StringRelatedField(many=True)
#     sentinel = serializers.StringRelatedField(many=True)
#     memcache = serializers.StringRelatedField(many=True)
#     es = serializers.StringRelatedField(many=True)
#     mcq = serializers.StringRelatedField(many=True)
#     tfs = serializers.StringRelatedField(many=True)
#     dev_owner = serializers.SerializerMethodField(read_only=True)
#     deploy_dir= serializers.SerializerMethodField(read_only=True)
#     zookeeper=serializers.StringRelatedField(many=True)
#     kafka=serializers.StringRelatedField(many=True)
#     mq=serializers.StringRelatedField(many=True)
#     mysql_slave = serializers.SerializerMethodField(read_only=True)
#     codis_slave = serializers.SerializerMethodField(read_only=True)
#     sentinel_slave = serializers.SerializerMethodField(read_only=True)
#     redis_slave = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Item_list
#
#
#     def get_dev_owner(self, obj):
#         return obj.item.dev_owner
#
#     def get_deploy_dir(self, obj):
#         return obj.item.location
#
#     def get_mysql_slave(self, obj):
#         result=[]
#         if obj.mysql_link.all().__len__()!=0:
#             for m in obj.mysql_link.all():
#                 result.extend([ x.name for x in m.slaveof.all() ])
#
#         return list(set(result))
#
#     def get_codis_slave(self, obj):
#         result=[]
#         if obj.codis_link.all().__len__()!=0:
#             for m in obj.codis_link.all():
#                 result.extend([ x.name for x in m.slaveof.all() ])
#
#         return list(set(result))
#
#     def get_sentinel_slave(self, obj):
#         result=[]
#         if obj.sentinel.all().__len__()!=0:
#             for m in obj.sentinel.all():
#                 result.extend([ x.name for x in m.slaveof.all() ])
#
#         return list(set(result))
#
#     def get_redis_slave(self, obj):
#         result=[]
#         if obj.redis_link.all().__len__()!=0:
#             for m in obj.redis_link.all():
#                 result.extend([ x.name for x in m.slaveof.all() ])
#
#         return list(set(result))