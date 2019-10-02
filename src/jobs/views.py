from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def about(request):
    
    return render(request, 'about1.html')

def contact(request):

    return render(request,'contact.html')

def index(request):

    return render(request,'index.html')

def rainbow_tick(request):

    return render(request,'rainbow_tick.html')