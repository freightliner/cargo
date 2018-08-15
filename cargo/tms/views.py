from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


from django.views.generic import FormView
from django.views.generic.base import TemplateView

def index(request):
    return render(request, 'tms/index.html')

def signin(request):
    
    username = request.POST['username']
    password = request.POST['password']
    
    print('usuario %s, password %s' % (username, password))
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'tms/index2.html')
    else:
        return render(request, 'tms/index.html')

def signout(request):
    logout(request)
    return render(request, 'tms/index.html')

def mm(request):
    return render(request, 'tms/mm.html')

class HomeView(TemplateView):
    template_name = 'tms/index2.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
#        messages.info(self.request, "hello http://example.com")
        return context