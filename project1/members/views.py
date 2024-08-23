from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world! CDTI")
# Create your views here.
def profile(request):
    return HttpResponse("Hello world! CDTI")
