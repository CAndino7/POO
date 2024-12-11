from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)
    id = models.CharField(max_length=25, unique=True,primary_key=True)
    lastName = models.CharField(max_length=25, blank= True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
 

class PaymentMetod(models.Model):
    
    bank = models.CharField(max_length=25)
    cardNum = models.CharField(max_length=16)
    cvsCode = models.CharField(max_length=4)
    expDate = models.DateTimeField()

class Client(User):
    address = models.CharField(max_length=200, null= True)
    paymentM = models.ForeignKey(PaymentMetod, on_delete=models.CASCADE)




class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.FloatField()

class Menu(models.Model):
     name = models.CharField(max_length=20)
     menu = models.ManyToManyField(MenuItem)

class Restaurant(User):
        address = models.CharField(max_length=200, null= True)
        phone2 = models.CharField(max_length=25, null= True)
        menu = models.ForeignKey(Menu, on_delete=models.CASCADE)



class Driver(User):
     makeModel = models.CharField(max_length=40, null= True)
     year = models.CharField(max_length=4, blank=True)        
     plateNum = models.CharField(max_length=12)

