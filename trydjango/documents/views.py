from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(*args, **kwargs): #args, kwargs
    return HttpResponse('<h1>Boldog Nevnapot Anita!</h1>') #string of html code

def contact_view(*args, **kwargs):
    return HttpResponse('<h1>Contact Page!</h1>') #string of html code