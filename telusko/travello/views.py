"""
VIEWS.py -> Business logic code 
We're in the views file of travello app. Over here we can: 
1. Make functions named after the .html files from the templates to display the frontend that we want. 
        The param of these functions should include "request" and should return statment could be -> render(request, specific_name.html, mapping of objects from the models.py to the html content)
2. Make objects of the classes made in the models file of travello app and include it in the return statement of the function.
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# passsing dynamic data in html via the functions in Views.py
def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = "The city that never sleeps, where Talash was shot"
    dest1.img = "destination_1.jpg"
    dest1.price = 700
    dest1.offer = False

    # dest1.desc = telusko/assets/images/destination_1.jpg

    dest2 = Destination()
    dest2.name = "Delhi"
    dest2.desc = "The city where gyal aint safe"
    dest2.img = "destination_2.jpg"
    dest2.price = 650
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "Banglore"
    dest3.desc = "Tech India"
    dest3.img = "destination_3.jpg"
    dest3.price = 750
    dest3.offer = True

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests}) 