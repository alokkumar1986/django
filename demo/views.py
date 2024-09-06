from django.shortcuts import render

# Create your views here.
def index(request):
    # context = {
    #     "firstname": "Aptech"
    # }
    # return render(request, 'index.html', context)
    
    # if(firstname == 'Aptech'):
    #     context = {
    #         "name" : "Aptech"
    #     }
    # else:
    #     context = {
    #         "name" : "World"
    #     }
    
    # context = {
    #     "name" : "Aptech1"
    # }
    data = [
        {
            "course" : "Python",
            "duration" : "2 months"        
        },
        {
            "course" : "Java",
            "duration" : "3 months"        
        }, 
        ]
    context = {
        "data": data
    }
    return render(request, 'index.html', context)
    
    
def aboutus(request):
    return render(request, 'aboutus.html')