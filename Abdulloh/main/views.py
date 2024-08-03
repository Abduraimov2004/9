from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()
    image = Team.objects.all()
    return render(request, 'index.html', {'services': services,
                                          'portfolio': portfolio,
                                          'image': image})
