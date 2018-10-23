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
#    model = Pai
    paginate_by = 15
    
    campos = {
            'q0paicod' : { 'n':'paicod', 'f':'istartswith'},
            'q0painom' : { 'n':'painom', 'f':'istartswith'},
            'q0paic3c' : { 'n':'paic3c', 'f':'istartswith'},
            'q0painum' : { 'n':'painum'},
            'q1paicod' : { 'n':'paicod', 'f':'gte'},
            'q2paicod' : { 'n':'paicod', 'f':'lte'},
            'q1painom' : { 'n':'painom', 'f':'istartswith'},
            'q1paic3c' : { 'n':'paic3c', 'f':'gte'},
            'q2paic3c' : { 'n':'paic3c', 'f':'lte'},
            'q1painum' : { 'n':'painum', 'f':'gte'},
            'q2painum' : { 'n':'painum', 'f':'lte'},
    }
    
    filtros = {}
    
    def procesar_filtros(self, request, campos):
        log.info('-----> Inicio')
        filtros = {}
        
        for f in request.GET.items():
            if len(f[1]) == 0:
                continue
            if f[0] in campos:
                c = campos[f[0]]
                nombre = c['n']
                if 'f' in c:
                    nombre += '__' + c['f']
                filtros[nombre] = f[1]
        
        log.info('     {}'.format(filtros))
        log.info('<----- Fin')
        return filtros
    
    def procesar_action(self, request):
        log.info('-----> Inicio')
        if not 'a' in request.GET:
            log.info('<----- Fin. No action')
            return
        
        if request.GET['a'] == 's':
            self.filtros = self.procesar_filtros(request, self.campos)
        
        log.info('<----- Fin')
        
    def get(self, request):
        log.info('-----> Inicio')
        
        self.procesar_action(request)
        
        response = super(Index, self).get(request)
        log.info('<----- Fin')
        return response
       
    def get_queryset(self):
        log.info('-----> Inicio')
        
        log.info('     (filtros): {}'.format(self.filtros))

        pais = Pai.objects.filter(**self.filtros)
        log.info('<----- Fin')        
        return pais
    
class Edit(generic.DetailView):
    model = Pai
    template_name = 'tms/pai.html'
    pk_url_kwarg = 'paicod'
    