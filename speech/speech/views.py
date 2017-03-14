from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import AudioForm


@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def results(request):
    return HttpResponse('results')

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'id': form.instance.id},status=200)
    return HttpResponse('')
