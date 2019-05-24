from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.serializers import serialize

from .models import Slope,Restaurant, Grenouillere, Parking, Lift

# Create your views here.
def status(request):
    return render(request, 'skiresort/status.html')

def difficulty(request):
    return render(request, 'skiresort/difficulty.html')

def infos(request):
    return render(request, 'skiresort/infos.html')


def slopesdata(request):
    slopes = Slope.objects.all()
    ser = serialize('geojson', slopes, geometry_field='geom', fields=('name', 'status',))

    return HttpResponse(ser)

def restaurantsdata(request):
    restaurants = Restaurant.objects.all()
    ser = serialize('geojson', restaurants, geometry_field='geom', fields=('name',))

    return HttpResponse(ser)

def grenouilleresdata(request):
    grenouilleres = Grenouillere.objects.all()
    ser = serialize('geojson', grenouilleres, geometry_field='geom', fields=('status',))

    return HttpResponse(ser)

def parkingsdata(request):
    parkings = Parking.objects.all()
    ser = serialize('geojson', parkings, geometry_field='geom', fields=('status',))

    return HttpResponse(ser)

def liftsdata(request):
    lifts = Lift.objects.all()
    ser = serialize('geojson', lifts, geometry_field='geom', fields=('name',))

    return HttpResponse(ser)