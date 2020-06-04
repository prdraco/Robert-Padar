from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Robert'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    val3 = int(request.POST['num3'])
    res = val1 + val2 + val3

    return render(request, 'contact.html', {'result':res})