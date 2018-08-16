from django.http import HttpResponse
from django.shortcuts import render

from tms.models import Pai

def index(request):
    objs = Pai.objects.all()
    context = {
            'listado' : objs,
            }
    return render(request, 'tms/pais.html', context)