# #coding=utf8
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from api.base.models import *
from .wiget import *

class LoginForm(AuthenticationForm):
    '''Authentication form which uses boostrap CSS.'''
    username = forms.CharField(max_length=255,widget=forms.TextInput({
                                   'class': 'form-control'}))
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput({
                                   'class': 'form-control'}))
