import logging

from django import forms

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from tms.models import Sec

logger = logging.getLogger(__name__)

class SecForm(forms.Form):
    seccod = forms.CharField(max_length = 20)
    secval = forms.IntegerField()
    secfmt = forms.CharField(max_length = 20)
    
    def is_valid(self):
        return True

def index(request):
    objs = Sec.objects.all()
    context = {
            'listado' : objs,
            }
    return render(request, 'tms/secs.html', context)

def edit(request, seccod):
    logger.info('-----> Inicio')
    obj = get_object_or_404(Sec, seccod=seccod)
    context = {
            'obj' : obj,
            }
    form = SecForm()
    form.seccod = obj.seccod
    form.secval = obj.secval
    form.secfmt = obj.secfmt
    context['form'] = form
    
    logger.info('<----- Fin')
    return render(request, 'tms/sec.html', context)

#def save(request, seccod):
#    
#    # aqui lo que sea
#    
#    
#    return index(request)

def save(request, seccod):
    logger.info('-----> Inicio')
    
    form = SecForm(request.POST)
    if not form.is_valid():
        logger.info('<----- Fin: not valid')
        return render(request, 'tms/sec.html', { 'form': form })


    logger.info('<----- Fin')
    return HttpResponseRedirect(reverse('tms:sec', args=()))

def savexx(request, seccod):
    entity = get_object_or_404(Sec, seccod=seccod)
    try:
        pass
    except (KeyError, Sec.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'tms/sec.html', {
            'question': entity,
            'error_message': "You didn't select a choice.",
        })
    else:
        entity.save()
        return HttpResponseRedirect(reverse('tms:sec', args=()))