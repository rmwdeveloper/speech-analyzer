from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import AudioForm
from chunkedUpload.forms import ChunkedUploadForm
from chunkedUpload.utils import concatenateChunks
# from transcriber.tasks import  myCallback

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

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        # form = AudioForm(request.POST, request.FILES)
        form = ChunkedUploadForm(request.POST, request.FILES)
        form.save()
        if request.POST['resumableChunkNumber'] == request.POST['resumableTotalChunks']:
            concatenateChunks(request.POST['resumableIdentifier'])
        return JsonResponse({'message': 'OK!'})
        # if form.is_valid():
        #     form.save()
        #     return JsonResponse({'id': form.instance.id, 'transcription': form.instance.documentTranscription},status=200)
        # return JsonResponse({'error': form.errors}, status=400)

    ## todo : check if chunk already exists to allow for upload resumation
    return HttpResponse(status=200)
