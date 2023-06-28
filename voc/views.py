from django.shortcuts import render, redirect
from django.http import JsonResponse

from users.decorators import login_required
from .exceltodb import exceltodb
from .forms import VOCForm
from .models import CustomerTB
# .filter(cent=request.user.uid.cent).order_by('receipt') 
## tmcheck
## get voc main page with voc data from dbCustomerTB
@login_required
def tmcheck(request):
    if request.method == 'GET':
        ## load voc but only for engineer's work center
        data = CustomerTB.objects.all()
        form = VOCForm()
        return render(request, 'voc/tmcheck.html', {'data': data,
                                                    'form': form,})
    ## get excel file and extract data to db    
    if request.method == 'POST':
        form = VOCForm(request.POST, request.FILES)
        if form.is_valid():
            _file = form.save()
            exceltodb(_file) ## extract data in VOCTB to CustomerTB
            return redirect('/')
        else:
            return JsonResponse({'message': 'Invalid form data'})


    
def voc(request):
    data = CustomerTB.object.all()
    return render(request, 'voc/tmcheck.html', {'data':data})