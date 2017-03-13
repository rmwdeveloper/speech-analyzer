from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def upload(request):
    return HttpResponse('Hello World')