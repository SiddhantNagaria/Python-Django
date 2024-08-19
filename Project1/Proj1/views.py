from django.shortcuts import render

# Create your views here.

def all_chai(request):
    return render(request, 'Proj1/all_chai.html')