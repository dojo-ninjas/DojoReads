from django.shortcuts import render, HttpResponse, redirect
from app1.models import *
from log_reg.models import *
from django.contrib import messages

def index(request):
    return render(request, 'log_reg/index.html')

def register(request):
    errors=User.objects.registerValidator(request.POST)
    if errors:
        for key,value in errors.items():
            messages.error(request, value,'register')
        request.session['errorType']='register'
        return redirect('/')
    else:
        User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=request.POST['password'])
        request.session['alias']=request.POST['alias']
        return redirect('/success')

def login(request):
    errors=User.objects.loginValidator(request.POST)
    if errors:
        for key,value in errors.items():
            messages.error(request, value,'login')
        request.session['errorType']='login'
        return redirect('/')
    else:
        emailFilter=User.objects.filter(email=request.POST['email'])
        user= emailFilter[0]
        request.session['alias']=user.alias
        return redirect('/success')

def userPage(request, my_id):
    user=User.objects.filter(id=my_id)
    context={
        'user':user[0],
        'reviews':Review.objects.filter(user__in=user),
        'reviewCount': Review.objects.filter(user__in=user).count()
    }
    return render(request, 'log_reg/user.html', context)

def success(request):
    return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect("/")