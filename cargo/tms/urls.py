from django.conf.urls import url

from tms.vistas import cliGest
from tms.vistas import paiGest
from tms.vistas import secGest

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^signin/$', views.signin, name='signin'),
        
        
        
        url(r'^cli/$', cliGest.index, name='cliGest'),
        url(r'^cli/(?P<id>[0-9]+)/$', cliGest.detail, name='cliGest.detail'),
        url(r'^cli/test/$', cliGest.test, name='cliGest.test'),
        
        url(r'^mm/$', views.mm, name='views-mm'),
        
        url(r'^pai/$', paiGest.index, name='paiGest'),
        url(r'^sec/$', secGest.index, name='secGest'),
]