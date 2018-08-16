from django.conf.urls import url

from tms.vistas import cliGest
from tms.vistas import paiGest
from tms.vistas import secGest

from . import views

app_name = 'tms'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^signin/$', views.signin, name='signin'),
        
        
        
        url(r'^cli/$', cliGest.index, name='cli'),
        url(r'^cli/(?P<id>[0-9]+)/$', cliGest.detail, name='cli.edit'),
        
        url(r'^mm/$', views.mm, name='views-mm'),
        
        url(r'^pai/$', paiGest.index, name='pai'),
        
        url(r'^sec/$', secGest.index, name='sec'),
        url(r'^sec/(?P<seccod>[a-zA-Z0-9]+)/$', secGest.edit, name='sec.edit'),
        url(r'^sec/(?P<seccod>[a-zA-Z0-9]+)/save/$', secGest.save, name='sec.save'),
        
        url('^home/$', views.HomeView.as_view(), name='home')
        
        
]