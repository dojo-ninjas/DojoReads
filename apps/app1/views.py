from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.app1.models import *
from apps.log_reg.models import *

def index(request):
    if 'alias' not in request.session:
        messages.error(request, 'You must be logged in to view this site')
        request.session['errorType']='notLoggedIn'
        return redirect('/')
    return render(request,'app1/index.html')
def addBook(request):
    if(request.method == 'GET'):
        return render(request,'app1/addBook.html')
    else:
        Book.objects.create(title=request.POST['title'], author=request.POST['author'])
        newBook=Book.objects.filter(title=request.POST['title'])
        loggedInUser=User.objects.filter(alias=request.session['alias'])
        Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user=loggedInUser[0], book=newBook[0])
        newReview=Review.objects.filter(review=request.POST['review'])
        return redirect(f'/books')
        # return redirect(f'/books/{newReview.id}')
