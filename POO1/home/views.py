from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html' , {})

def base(request):
    return render(request ,'base.html', {})

def test(request):
    return render(request, 'test.html', {} )

def new(request):
    return render(request, 'new.html' , {})