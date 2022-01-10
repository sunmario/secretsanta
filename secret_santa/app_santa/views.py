from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ping(request):
    response = "200 OK"
    return HttpResponse(response)

