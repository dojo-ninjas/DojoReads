from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("App 1 urls are set up correctly")