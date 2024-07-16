from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("Eat no meat!")

def february(request):
    return HttpResponse("Run for 15 minutes everyday!")