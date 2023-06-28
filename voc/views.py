from django.shortcuts import render
from django.http import JsonResponse

from users.decorators import login_required
from .exceltodb import exceltodb
from .forms import VOCForm

@login_required
def tmcheck(request):
    if request.method == 'GET':
        form = VOCForm()
        return render(request, 'voc/tmcheck.html', {'form': form})
    if request.method == 'POST':
        form = VOCForm(request.POST, request.FILES)
        if form.is_valid():
            _file = form.save()
            exceltodb(_file) ## extract data in VOCTB to CustomerTB
            return JsonResponse({'message': 'Upload success'})
        else:
            return JsonResponse({'message': 'Invalid form data'})
    return JsonResponse({'message': 'Upload failed'})
    
    
@login_required
def upload_voc(request):
    if request.method == 'POST' and request.FILES['cstr_file']:
        form = VOCForm(request.POST, request.FILES)
        if form.is_valid():
            _file = form.save()
            exceltodb(_file) ## extract data in VOCTB to CustomerTB
            return JsonResponse({'message': 'Upload success'})
        else:
            return JsonResponse({'message': 'Invalid form data'})
    return JsonResponse({'message': 'Upload failed'})

