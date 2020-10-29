from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getData(request):
    if request.method == "POST":
        return JsonResponse({"hello": "Post request placed"})
    return JsonResponse({"hello" : "my first api"})