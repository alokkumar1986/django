from urllib import request
from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.template import loader

from mysite.models import Contact
from django.views.decorators.csrf import csrf_protect, requires_csrf_token, ensure_csrf_cookie


# Create your views here.

def index(request) :
    template = loader.get_template('index.html')
    return HttpResponse(template.render({"title": "Home"}))

def aboutus(req):
     template = loader.get_template('aboutus.html')
     return HttpResponse(template.render({"title": "Aboutus"}))

def contactus(request):
    # template = loader.get_template('contactus.html')
    contact = Contact.objects.all().values()
    context = {"context": contact}
    return render(request, 'contactus.html', context)

@csrf_protect
def savecontact(request):
    id = int(request.POST['id'])
    name = request.POST['name']
    email = request.POST['email']
    mobile = request.POST['mobile']
    contact = Contact(id, name, email,  mobile)
    contact.save()
    return redirect('contactus')
