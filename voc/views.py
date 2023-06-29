from django.shortcuts import render, redirect
from django.http import JsonResponse
import magic

from users.decorators import login_required
from .exceltodb import exceltodb
from .forms import VOCForm
from .models import CustomerTB

## tmcheck
## get voc main page with voc data from dbCustomerTB
@login_required
def tmcheck(request):
    if request.method == 'GET':
        ## load voc but only for engineer's work center
        data = CustomerTB.objects.filter(cent=request.user.uid.cent).order_by('receipt')
        form = VOCForm()
        return render(request, 'voc/tmcheck.html', {'data': data,
                                                    'form': form,})
    ## get excel file and extract data to db    
    if request.method == 'POST':
        try:
            mime_type = magic.from_buffer(request.FILES.read(1024), mime=True)
            if mime_type == 'application/vnd.ms-excel':
                form = VOCForm(request.POST, request.FILES)
                if form.is_valid():
                    _file = form.save()
                    exceltodb(_file) ## extract data in VOCTB to CustomerTB
                    return redirect('/')
                else:
                    return JsonResponse({'message': 'Invalid form data'})
            elif mime_type == 'audio/mpeg':
                return None ## insert AI code here
        except:
            ## if the file is not .xls, .mp3
            return JsonResponse({'message': 'Invalid file type'})
    
def voc(request):
    data = CustomerTB.object.all()
    return render(request, 'voc/tmcheck.html', {'data':data})