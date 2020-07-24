from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs): #args, kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse('<h1>Boldog Nevnapot Anita!</h1>') #string of html code
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_content = {
        'my_text': 'This is about us!',
        'my_number': 123,
        'my_list': [231,632,36,41,50, 'Rob'],
    }
    return render(request, 'about.html', my_content)
