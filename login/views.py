from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect, requires_csrf_token, ensure_csrf_cookie

# Create your views here.

def index(request): 
    return render(request, 'index.html')

@csrf_protect
def doLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    
    if not username :
       context = {
            'usernamemessage' : "Username canot be blank.",
            'passmessage' : "",
            'values' : {
                'username': username,
                'password' : password
            } 
           }
       return render(request, 'index.html', context)  
    if not password :
       context = {
            'usernamemessage' : "",
            'passmessage' : "Password canot be blank." ,
            'values' : {
                'username': username,
                'password' : password
            }
           }
       return render(request, 'index.html', context)  
    
    if User.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)
        if user is None:
          context = {
            'message' : "Invalid Username and Password" 
           }
          return render(request, 'index.html', context)  
        else:    
         login(request, user)    
         return redirect('home')
    else :
        context = {
            'message' : "Invalid Username" 
        }
        return render(request, 'index.html', context)

@login_required
#@permission_required
def home(request):
    return render(request, 'home.html')