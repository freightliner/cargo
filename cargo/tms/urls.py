from django.conf.urls import url
from django.views.generic.base import TemplateView

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
        
        url(r'^pai/$', paiGest.Index.as_view(), name='pai'),
        url(r'^pai/(?P<paicod>[a-zA-Z0-9]+)/$', paiGest.Edit.as_view(), name='pai.edit'),
        url(r'^paiadd/$', paiGest.Edit.as_view(), name='pai.add'),
        url(r'^paias/$', TemplateView.as_view(template_name='tms/paias.html'), name='pai.as'),
        
        #url(r'^pai/$', paiGest.index, name='pai'),
        #url(r'^pai/(?P<paicod>[a-zA-Z0-9]+)/$', paiGest.edit, name='pai.edit'),
        url(r'^pai/(?P<paicod>[a-zA-Z0-9]+)/save/$', paiGest.save, name='pai.save'),
        
        # ^\S+$
        
        url(r'^sec/$', secGest.index, name='sec'),
        url(r'^sec/(?P<seccod>[a-zA-Z0-9]+)/$', secGest.edit, name='sec.edit'),
        url(r'^sec/(?P<seccod>[a-zA-Z0-9]+)/save/$', secGest.save, name='sec.save'),
        
        url('^home/$', views.HomeView.as_view(), name='home')
        
        
]