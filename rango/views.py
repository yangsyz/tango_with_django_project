from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = "Rango says hey there partner!" + '<a href="/rango/about/">About</a>'
    return HttpResponse(html)

def about(request):
    html = "Rango says here is the about page." + '<a href="/rango/">Index</a>'
    return HttpResponse(html)
# Create your views here.
