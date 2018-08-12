from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

def index(request):
    return render(request, 'tms/index.html')

def signin(request):
    
    username = request.POST['username']
    password = request.POST['password']
    
    print('usuario %s, password %s' % (username, password))
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'tms/mm.html')
    else:
        return render(request, 'tms/index.html')

def signout(request):
    logout(request)
    return render(request, 'tms/index.html')








def mm(request):
    return render(request, 'tms/mm.html')