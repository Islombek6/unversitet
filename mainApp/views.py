from django.shortcuts import render
from datetime import datetime

from .models import *


def home_view(request):
    today = datetime.today()
    context = {
        'today': today,
    }
    return render(request, 'home.html', context)

def fan_view(request):
    fanlar = Fan.objects.all()
    contex = {
        'fanlar': fanlar,
    }
    return render(request, 'fanlar.html', contex)
