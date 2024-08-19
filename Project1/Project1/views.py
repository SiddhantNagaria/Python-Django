from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello World. I am Siddhant Nagaria- Home Page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello World. I am Siddhant Nagaria- About Page")

def contact(request):
    return HttpResponse("Hello World. I am Siddhant Nagaria- Contact Page")