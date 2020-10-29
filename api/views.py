from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.



def getData(response):
    return JsonResponse({"hello" : "my first api"})