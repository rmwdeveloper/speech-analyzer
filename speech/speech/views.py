from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def test_celery(request):
    # test.apply_async(link=myCallback.s())
    return HttpResponse('test_celery')

@csrf_exempt
def results(request):
    return HttpResponse('results')


