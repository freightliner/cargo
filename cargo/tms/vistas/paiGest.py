import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from tms.models import Pai

log = logging.getLogger(__name__)

def indexxx(request):
    log.info('-----> Inicio')
    objs = Pai.objects.all()
    context = {
            'listado' : objs,
            }
    log.info('<----- Fin')
    return render(request, 'tms/pais.html', context)

def edit(request, paicod):
    log.info('-----> Inicio')
    log.info('       (paicod): {}'.format(paicod))
    obj = get_object_or_404(Pai, paicod=paicod)
    log.info('<----- Fin')
    return render(request, 'tms/pai.html', { 'obj': obj})

def save(request, paicod):
    log.info('-----> Inicio')
    log.info('       (paicod): {}'.format(paicod))
    log.info('<----- Fin')
    return HttpResponseRedirect(reverse('tms:pai', args=()))

class Index(generic.ListView):
    
    template_name = 'tms/pais.html'
    model = Pai
    #context_object_name = 'listado'
    paginate_by = 50
    
    campos = {
            'q0paicod' : { 't' : 'string', 'v' : None },
            'q0painom' : { 't' : 'string', 'v' : None },
    }
    
    def get_queryset(self):
        log.info('-----> Inicio')
        
        log.info(self.request.GET)
#        qd = self.request.GET.QueryDict
#        log.info(qd)
        
        log.info('<----- Fin')
        return Pai.objects.all()
    
class Edit(generic.DetailView):
    model = Pai
    template_name = 'tms/pai.html'
    pk_url_kwarg = 'paicod'
    