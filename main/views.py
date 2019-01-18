from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/list/index.html',{})



def business_kpi(request):
    return render(request, 'main/list/business_kpi.html',{})    