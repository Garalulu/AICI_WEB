from django.shortcuts import render
from django.http import JsonResponse

from users.decorators import login_required
from .forms import ConstructionForm

@login_required
def construction(request):
    if request.method == 'GET':
        return render(request, 'construction/construction.html')
    
@login_required
def upload_construction(request):
    if request.method == 'POST' and request.FILES['file']:
        form = ConstructionForm(request.POST, request.FILES)
        if form.is_valid():
            _file = form.save()
           
            return JsonResponse({'message': 'Upload success'})
    return JsonResponse({'message': 'Upload failed'})
