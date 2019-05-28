from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Slope,Restaurant, Grenouillere, Parking, Lift

# View Status
def status(request):
    return render(request, 'skiresort/status.html')

# View difficulty
def difficulty(request):
    return render(request, 'skiresort/difficulty.html')

# View informations
def infos(request):
    return render(request, 'skiresort/infos.html')

# Get all the data of the slopes
def slopesdata(request):
    slopes = Slope.objects.all()
    ser = serialize('geojson', slopes, geometry_field='geom', fields=('name', 'statrus', 'difficulty', 'altstart', 'altarrival', 'difheight', ))
    return HttpResponse(ser)

# Get all the data of the restaurants
def restaurantsdata(request):
    restaurants = Restaurant.objects.all()
    ser = serialize('geojson', restaurants, geometry_field='geom', fields=('name', 'status', 'altitude', 'capacity'))
    return HttpResponse(ser)

# Get all the data of the grenouillères
def grenouilleresdata(request):
    grenouilleres = Grenouillere.objects.all()
    ser = serialize('geojson', grenouilleres, geometry_field='geom', fields=('status', 'capacity', 'altitude', 'nbrperson', 'type', ))
    return HttpResponse(ser)

# Get all the data of the parkings
def parkingsdata(request):
    parkings = Parking.objects.all()
    ser = serialize('geojson', parkings, geometry_field='geom', fields=('status', 'altitude', 'capacity'))
    return HttpResponse(ser)

# Get all the data of the lifts
def liftsdata(request):
    lifts = Lift.objects.all()
    ser = serialize('geojson', lifts, geometry_field='geom', fields=('name', 'status', 'length', 'avgqueue', 'altstart', 'altarrival', 'maxflow', 'seatchair'))
    return HttpResponse(ser)