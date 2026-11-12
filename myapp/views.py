from django.http import request
from django.shortcuts import render,redirect
from myapp.models import *

def error(reguest):
    return render(request,'error.html')
def details(reguest):
    return render(request,'blog-details.html')
def blog(reguest):
    return render(request,'blog.html')
from django.shortcuts import render

def index(request):
    if request.method== 'POST':
        mycontact=Contact1(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/index')
    else:
        return render(request,'index.html')

    
def portfolio(reguest):
    return render(request,'portfolio-details.html')
def service(reguest):
    return render(request,'service-details.html')
def starter(reguest):
    return render(request,'starter-page.html')

def show(reguest):
   all=Contact1.objects.all()
   return render(reguest,'show.html',{'all':all})

