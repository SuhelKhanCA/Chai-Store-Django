from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World. You are at ChaiAurCode. This is HOME page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello World. You are at ChaiAurCode. This is ABOUT page")

def contact(request):
    return HttpResponse("Hello World. You are at ChaiAurCode. This is CONTACT page")
