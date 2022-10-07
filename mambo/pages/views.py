from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,'home.html',{})

def contact_view(request, *args, **kwargs):
    return render(request,'contact.html',{})

def social_view(request, *args, **kwargs):
    return render(request,'social.html',{})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "THis is me",
        "this_is_true": True,
        "my_number": "587",
        "my_list": [1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'about.html', my_context)
