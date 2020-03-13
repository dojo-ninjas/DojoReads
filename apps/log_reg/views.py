from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'log_reg/index.html')

def register(request):
    errors=User.objects.registerValidator(request.POST)
    if errors:
        for key,value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=request.POST['password'])
        request.session['alias']=request.POST['alias']
        return redirect('/success')

def login(request):
    errors=User.objects.loginValidator(request.POST)
    if errors:
        for key,value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        user=User.objects.filter(email=request.POST['email'])
        print(user[0])
        request.session['alias']=user[0].alias
        return redirect('/success')

def success(request):
    return render(request, 'log_reg/success.html')

def logout(request):
    request.session.flush()
    return redirect("/")