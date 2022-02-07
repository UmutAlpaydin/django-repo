from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
import requests
from .forms import Operation

# Create your views here.
@api_view(['GET', 'POST'])
def firstView(request):
    print(request.POST)
    first = request.POST.get('bir')
    second = request.POST.get('iki')
    context = {}
    
    return render(request, 'operation/index.html', context = {"form": Operation})


