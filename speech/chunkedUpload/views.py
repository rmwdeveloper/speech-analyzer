from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from chunkedUpload.forms import ChunkedUploadForm
from chunkedUpload.models import ChunkedUpload
from chunkedUpload.utils import concatenateChunks
from chunkedUpload.tasks import cleanupBlobs




@csrf_exempt
def upload(request):
    if request.method == 'POST':
        # form = AudioForm(request.POST, request.FILES)
        form = ChunkedUploadForm(request.POST, request.FILES)
        form.save()
        # if request.POST['resumableChunkNumber'] == request.POST['resumableTotalChunks']:
        #     concatenateChunks(request.POST['resumableIdentifier'])
        return JsonResponse({'message': 'OK!'})
        # if form.is_valid():
        #     form.save()
        #     return JsonResponse({'id': form.instance.id, 'transcription': form.instance.documentTranscription},status=200)
        # return JsonResponse({'error': form.errors}, status=400)

    ## todo : check if chunk already exists to allow for upload resumation
    return HttpResponse(status=200)


@csrf_exempt
def upload_complete(request):
    upload_id = request.POST.get('uploadId', '')
    concatenateChunks(upload_id)
    return HttpResponse(status=200)
    # t0 = ChunkedUpload.objects.all()
    # for obj in t0:
    #     obj.delete()
    # return HttpResponse(200)