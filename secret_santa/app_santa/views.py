from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ping(request):
    response = "OK"
    return HttpResponse(response)

