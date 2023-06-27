from django.shortcuts import render
from django.http import JsonResponse

from users.decorators import login_required
from .exceltodb import exceltodb
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
            _file = form.save()
            exceltodb(_file) ## extract data in VOCTB to CustomerTB
            return JsonResponse({'message': 'Upload success'})
    return JsonResponse({'message': 'Upload failed'})

def customer_list(request):
    if request.method == 'GET':
        customers = BoardTB.objects.all()
        data = []

        for customer in customers:
            customer_data = {
                'cust_name': customer.cust_name,
                'declaration': customer.declaration,
                'cust_type': customer.cust_type,
                'cust_num': customer.cus_num,
                'brd_updateust_ads': customer.brd_updateust_ads,
            }
            data.append(customer_data)

        return JsonResponse(data, safe=False)