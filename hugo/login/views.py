from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def log_in (request):
    if request.method == 'GET':    
        context = {'form' : AuthenticationForm }
        return render(request, 'log_in.html', context)
    elif request.method == 'POST':
        form = AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect('/')
            return HttpResponse("sure bud")
    else:
        return HttpResponse('Log in Error')    
    
def sign_up (request):    
    if request.method == 'GET':    
        context = {'form' : UserCreationForm }
        return render(request, 'sign_up.html', context)
    elif request.method == 'POST':
        form = UserCreationForm(request, request.POST)
        if form.is_valid():
            form.save()
            messages(request, 'Account created successfully')
            return redirect('home')
        
def test(request):
    return render(request, 'test.html', {})        

def base(request):
    return render(request, 'base.html', {}) 

def newuser(request):
    if request.method == 'GET':    
        context = {'form' : UserCreationForm }
        return render(request, 'newuser.html', context)
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages(request, 'Account created successfully')
            return redirect('home')