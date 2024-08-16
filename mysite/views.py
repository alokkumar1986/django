from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader


# Create your views here.

def index(request) :
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def aboutus(request):
     template = loader.get_template('aboutus.html')
     return HttpResponse(template.render())

def contactus(request):
    template = loader.get_template('contactus.html')
    return HttpResponse(template.render())