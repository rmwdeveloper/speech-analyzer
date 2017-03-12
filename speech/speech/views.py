from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def upload(request):
    return JsonResponse({'foo': 'bar'})