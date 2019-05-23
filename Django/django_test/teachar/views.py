from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def withparam(request,num):
    return HttpResponse(num)