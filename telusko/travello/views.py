"""
VIEWS.py -> Business logic code 
We're in the views file of travello app. Over here, we can instantiate the objects from classes made in the models file of travello app.
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The city that never sleeps, where Talash was shot"
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Delhi"
    dest2.desc = "The city where gyal aint safe"
    dest2.price = 300

    dest3 = Destination()
    dest3.name = "Vellore"
    dest3.desc = "The city where I didn't get placed. Lol look at me now 💸. ALHAMDULILLAH!"
    dest3.price = 10000

    return render(request, 'index.html', {'dest1': dest1, 'dest2': dest2, 'dest3': dest3 })

def contact(request):
    return render(request, 'contact.html')