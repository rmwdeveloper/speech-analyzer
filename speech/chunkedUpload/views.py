from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from chunkedUpload.forms import ChunkedUploadForm
from chunkedUpload.utils import concatenateChunks




@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = ChunkedUploadForm(request.POST, request.FILES)
        form.save()
        return JsonResponse({'message': 'OK!'})

    ## todo : check if chunk already exists to allow for upload resumation
    return HttpResponse(status=200)


@csrf_exempt
def upload_complete(request):
    upload_id = request.POST.get('uploadId', '')
    concatenateChunks(upload_id)
    return HttpResponse(status=200)
