from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
from .ocr import perform_ocr

def imagetoText(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image = Image.open(image)
        text = perform_ocr(image)
        return JsonResponse({'status': 'success', 'text': text})
    return render(request, 'imagetotext.html')
