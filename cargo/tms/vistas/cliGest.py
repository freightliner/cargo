from django.http import HttpResponse, Http404
from django.shortcuts import render

from tms.models import Cli

def index(request):
    clis = Cli.objects.all()
    context = {
            'listado' : clis,
            }
    return render(request, 'tms/clis.html', context)





def detail(request, id):
    return HttpResponse("Estás buscando el cliente %s." % id)

def test(request):
    
    from tms.models.SecBL import SecBL
    
    id1 = SecBL().next('id1')
    id2 = SecBL().next('id2')
    
#    raise Http404('esto es una excepcion')
    
    id3 = SecBL().next('id3')
    
    return HttpResponse("Estás buscando el cliente %s %s %s." % (id1, id2, id3))