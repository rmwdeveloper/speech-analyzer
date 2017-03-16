from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import AudioForm

from transcriber.tasks import test, myCallback

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def test_celery(request):
    test.apply_async(link=myCallback.s())
    return HttpResponse('test_celery')

@csrf_exempt
def results(request):
    return HttpResponse('results')

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'id': form.instance.id, 'transcription': form.instance.documentTranscription},status=200)
        return JsonResponse({'error': form.errors}, status=400)
    return HttpResponse(status=405)
