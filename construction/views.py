from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone

from users.decorators import login_required
from AICI_WEB.AI_mp3todb import construction
from .forms import ConstructionCallForm
from .models import ConstructionTB


@login_required
def construction(request):
    if request.method == 'GET':
        now = timezone.now()
        
        ## load constructions but only for engineer's work center
        _data = ConstructionTB.objects.filter(cent=request.user.uid.cent).order_by('receipt') 
        data = _data.filter(receipt__lte=now)
        return render(request, 'construction/construction.html', {'data': data})
    
@login_required
def upload_construction(request):
    if request.method == 'POST':
        form = ConstructionCallForm(request.POST, request.FILES)
        if form.is_valid():
            _file = form.save()
            receipt, cstr_company, cstr_location = construction(request.FILES)
            _call = ConstructionTB(receipt=receipt,
                                  cstr_company=cstr_company,
                                  cstr_location=cstr_location,
                                  cent=request.user.uid.cent,
                                  cstrcall=_file)
            _call.save()
           
            return redirect('/')
    return JsonResponse({'message': 'Upload failed'})
