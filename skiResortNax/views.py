from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.serializers import serialize

from .models import Slope

# Create your views here.
def status(request):
    return render(request, 'skiresort/status.html')

def difficulty(request):
    return render(request, 'skiresort/difficulty.html')

def infos(request):
    return render(request, 'skiresort/infos.html')


def slopesdata(request):
    slopes = Slope.objects.all()
    ser = serialize('geojson', slopes, geometry_field='geom', fields=('name',))

    return HttpResponse(ser)