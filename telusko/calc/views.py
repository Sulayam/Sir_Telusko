# Welcome to -views-, this is where we code the busniess logic for differenet URLS in this application we're currently in (calc).
    # So basically, we use the views.py to link the urls to its templates (UI) and Model (database). Views is the middleman between the url that
    # the user visits and the model(data) + template(Layout) that will be given back to the user. This is the MVT Framework

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Sulay 🛩️'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'output': res})