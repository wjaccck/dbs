# #coding=utf8
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)

class BaseSearchFieldMixin(object):
    pass

class BaseModelSelect2MultipleWidget(BaseSearchFieldMixin, ModelSelect2MultipleWidget):
    pass

class BaseModelSelect2Widget(BaseSearchFieldMixin, ModelSelect2Widget):
    pass

class IDCModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'name__istartswith',
        'pk__startswith',
    ]

class StatusModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'name__istartswith',
        'pk__startswith',
    ]


class Machine_typeModelSelect2Widget(BaseModelSelect2Widget):
    search_fields = [
        'name__istartswith',
        'pk__startswith',
    ]
# class IDCModelSelect2MultipleWidget(BaseModelSelect2MultipleWidget):
#     search_fields = [
#         'name__istartswith',
#         'pk__startswith',
#     ]

