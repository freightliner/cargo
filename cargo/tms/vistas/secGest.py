from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from tms.models import Sec

def index(request):
    objs = Sec.objects.all()
    context = {
            'listado' : objs,
            }
    return render(request, 'tms/secs.html', context)

def edit(request, seccod):
    obj = get_object_or_404(Sec, seccod=seccod)
    context = {
            'obj' : obj,
            }
    
    return render(request, 'tms/sec.html', context)

#def save(request, seccod):
#    
#    # aqui lo que sea
#    
#    
#    return index(request)

def save(request, seccod):
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