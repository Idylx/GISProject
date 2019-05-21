from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.serializers import serialize

# Create your views here.
def status(request):
    return render(request, 'status.html')

def difficulty(request):
    return render(request, 'difficulty.html')

def infos(request):
    return render(request, 'infos.html')