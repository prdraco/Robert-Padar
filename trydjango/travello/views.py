from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Paris'
    dest1.desc = 'Nulla pretium tincidunt felis, nec.'
    dest1.price = 399
    dest1.image = 'destination_4.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Bali'
    dest2.desc = 'The city that never sleeps'
    dest2.price = 699
    dest2.image = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'San Francisco'
    dest3.desc = 'Nulla pretium tincidunt felis, nec.'
    dest3.price = 559
    dest3.image = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
