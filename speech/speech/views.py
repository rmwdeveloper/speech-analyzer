from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def create_request(request):
    return JsonResponse({'foo': 'bar'})