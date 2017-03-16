from django.conf.urls import include, url
from webui.views import index
from webui.forms import LoginForm
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$',index,name='index'),

    url(r'^base/', include('webui.baseui.urls')),

    url(r'^login/$',
        login,
        {
            'template_name': 'webui/login.html',
            'authentication_form': LoginForm,

        },
        name='login',),

    # Django Select2
    url(r'^select2/', include('django_select2.urls')),

    url(r'^logout/$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),
]
