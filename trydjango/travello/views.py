from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Paris'
    dest1.desc = 'The city that never sleeps'
    dest1.price = 399

    return render(request, 'index.html', {'dest1': dest1})
