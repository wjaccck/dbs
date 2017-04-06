from django import http
import json
import sys
from django.views.debug import technical_500_response
from django.conf import settings
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    def process_view(self,request, view_func, view_args, view_kwargs):
        if view_func.__name__ in ['index','login','logout']:
            return None
        if request.user.username=='admin':
            return None
        else:
            return HttpResponseBadRequest(" {0} Do not have the access ".format(request.user.username))
    def __call__(self, request):
        response = self.get_response(request)
        return response
