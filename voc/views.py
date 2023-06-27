from django.shortcuts import render
from django.http import JsonResponse

from users.decorators import login_required
from .forms import VOCForm


@login_required
def tmcheck(request):
    if request.method == 'GET':
        return render(request, 'voc/tmcheck.html')
    
@login_required
def upload_voc(request):
    if request.method == 'POST' and request.FILES['file']:
        form = VOCForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Upload success'})
    return JsonResponse({'message': 'Upload failed'})

