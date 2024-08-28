from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, requires_csrf_token, ensure_csrf_cookie


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
    # template = loader.get_template('member.html')
    # return HttpResponse(template.render())
    return render(request, 'member.html')

@csrf_protect
def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1+num2
    context = {
        'result' : result
    }
    # template = loader.get_template('result.html')
    # return HttpResponse(template.render(result, request))
    return render(request, 'result.html', context)