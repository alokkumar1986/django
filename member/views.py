from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request) :
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
    context = {
        'name' : "Aptech Learning",
        'course' : 'Django'
    }
    return render(request, 'home.html', context)

def member(request):
    template = loader.get_template('member.html')
    return HttpResponse(template.render())

def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    result = num1+num2
    context = {
        'result' : result
    }
    # template = loader.get_template('result.html')
    # return HttpResponse(template.render(result, request))
    return render(request, 'result.html', context)