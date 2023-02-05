from django.db import models
from django import forms
# Create your models here.

class contactform(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    message=models.TextField()




class carousel(models.Model):
    image=models.FileField( upload_to='home/', max_length=400,null=True,default=None)
    imgtitle=models.CharField(max_length=100)
    imginto=models.CharField(max_length=100)




class defaultcarousel(models.Model):
    image=models.FileField( upload_to='home/defaultslider/', max_length=400,null=True,default=None)
    imgtitle=models.CharField(max_length=100)
    imginto=models.CharField(max_length=100)


class servicecard(models.Model):
    image=models.FileField( upload_to='card/', max_length=400,null=True,default=None)
    imgtitle=models.CharField(max_length=100,default=None)
    imginto=models.CharField(max_length=300,default=None)
    link=models.CharField( max_length=50,default=None)
    





