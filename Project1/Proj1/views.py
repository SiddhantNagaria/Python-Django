from django.shortcuts import get_object_or_404, render

from .models import ChaiVariety

# Create your views here.

def all_chai(request):
  chais = ChaiVariety.objects.all()
  return render(request, 'Proj1/all_chai.html', {'chais': chais})


def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id)
  return render(request, 'Proj1/chai_detail.html', {'chai': chai})