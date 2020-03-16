from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    if 'alias' not in request.session:
        messages.error(request, 'You must be logged in to view this site')
        return redirect('/')
    return render(request,'app1/index.html')