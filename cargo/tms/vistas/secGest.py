from django.shortcuts import render

from tms.models import Sec

def index(request):
    objs = Sec.objects.all()
    context = {
            'listado' : objs,
            }
    return render(request, 'tms/secs.html', context)