from django.urls import path
from . import views

urlpatterns=[
path('base/',views.base, name= 'base layout'),
path('home/', views.home, name= 'home page'),
path('test/', views.test , name ='test' ),
path('new/', views.new, name= 'new user')
]