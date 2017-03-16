#coding=utf8
from django.shortcuts import render,redirect



def index(req):
    if req.user.is_authenticated():
        response = render(req,'webui/index.html'
                          )
    else:
        response =redirect('login')
    return response