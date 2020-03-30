from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from app1.models import *
from log_reg.models import *
import datetime

def index(request):
    if 'alias' not in request.session:
        messages.error(request, 'You must be logged in to view this site')
        request.session['errorType']='notLoggedIn'
        return redirect('/')
    allReviews=Review.objects.all()
    context={
        'allReviews':allReviews,
        'lastThree':allReviews.order_by('-id')[:3]
    }
    return render(request,'app1/index.html', context)
def addBook(request):
    if(request.method == 'GET'):
        context={
            'allAuthors':Book.objects.order_by().values('author').distinct()
        }
        return render(request,'app1/addBook.html', context)
    else:
        if(request.POST['existingAuthor']=='Select the Author'):
            author=request.POST['newAuthor']
        else:
            author=request.POST['existingAuthor']

        Book.objects.create(title=request.POST['title'], author=author)
        newBook=Book.objects.filter(title=request.POST['title'])
        loggedInUser=User.objects.filter(alias=request.session['alias'])
        Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user=loggedInUser[0], book=newBook[0])
        newReview=Review.objects.filter(review=request.POST['review'])
        return redirect(f'/books')
        # return redirect(f'/books/{newReview.id}')
