from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name = 'home'),
    path('sign_up/', views.sign_up, name = 'sign up'),
    path('test/', views.test, name = 'test'),
    path('newuser/', views.newuser, name = 'new user'),
    path('base/', views.base, name = 'base')
]