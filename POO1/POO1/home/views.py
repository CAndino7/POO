from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Client

# Create your views here.

def home(request):
    return render(request, 'home.html' , {})

def base(request):
    return render(request ,'base.html', {})

def test(request):
    return render(request, 'test.html', {} )

def new(request):
    return render(request, 'new.html' , {})

def userpassword(request):
    if request.method == 'GET':    
        context = {'form' : AuthenticationForm }
        return render(request, 'userpassword.html', context)
    elif request.method == 'POST':
        form = AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            user = form.get_user()
            user.save()
            return redirect('home.html')
    else:
        return HttpResponse('Log in Error')    

def newclient(request):
    if request.method == 'GET':    
        context = {'form' : UserCreationForm }
        return render(request, 'newclient.html', context)
    elif request.method == 'POST':
        form = UserCreationForm(request, data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('test.html')
    else:
        return HttpResponse('Log in Error')   


def newrest(request):
    if request.method == 'GET':    
        context = {'form' : UserCreationForm }
        return render(request, 'newrest.html', context)
    elif request.method == 'POST':
        form = UserCreationForm(request, data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home.html')
    else:
        return HttpResponse('Log in Error')

def newdriver(request):
    if request.method == 'GET':    
        context = {'form' : UserCreationForm }
        return render(request, 'newdriver.html', context)
    elif request.method == 'POST':
        form = UserCreationForm(request, data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home.html')
    else:
        return HttpResponse('Log in Error')
    
def dashclient(request):
    clients = Client.objects.all()
    
