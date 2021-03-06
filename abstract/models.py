from django.db import models


# Base models that have some common fields.

class CommonModel(models.Model):
    # Meta data for one object.
    created_date = models.DateTimeField(auto_now_add=True,db_index=True)
    modified_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.user', related_name='%(app_label)s_%(class)s_creator', verbose_name='creator')
    last_modified_by = models.ForeignKey('auth.user', related_name='%(app_label)s_%(class)s_last_modified_by',
                                         verbose_name='last modified by')

    class Meta:
        abstract = True

class NameModel(models.Model):
    name = models.CharField(max_length=80, unique=True)
    # Meta data for one object.
    creator = models.ForeignKey('auth.user', related_name='%(app_label)s_%(class)s_creator', verbose_name='creator')
    last_modified_by = models.ForeignKey('auth.user', related_name='%(app_label)s_%(class)s_last_modified_by', verbose_name='last modified by')
    created_date = models.DateTimeField(auto_now_add=True,db_index=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class BASE_FATHER(models.Model):
    pass
    @staticmethod
    def father():
        return u'base'

    class Meta:
        abstract=True
#

class ASSETS_FATHER(models.Model):
    pass
    @staticmethod
    def father():
        return u'assets'

    class Meta:
        abstract=True
class RESOURCE_BASE(models.Model):
    pass
    @staticmethod
    def father():
        return u'resource'

    class Meta:
        abstract=True
#
# class ITEM_BASE(models.Model):
#     pass
#     @staticmethod
#     def father():
#         return u'item'
#
#     class Meta:
#         abstract=True
#
# class APPLY_BASE(models.Model):
#     pass
#     @staticmethod
#     def father():
#         return u'apply'
#
#     class Meta:
#         abstract=True
#
#
# class HISTORY_BASE(models.Model):
#     pass
#     @staticmethod
#     def father():
#         return u'history'
#
#     class Meta:
#         abstract=True

