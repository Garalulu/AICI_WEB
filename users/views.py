from django.contrib import auth
from django.shortcuts import render
from django.http import JsonResponse

from .models import EngineerTB


# Create your views here.
def login(request):
    return render(request, 'login.html')

def join(request):
    ## Default page load
    if request.method == 'GET':
        return render(request, 'join.html')
    
    ## Signup request
    if request.method == 'POST':
        if request.POST['inputPassword'] == request.POST['inputPasswordCk']:
            try:
                new_user = EngineerTB.objects.create_user(usr_id=request.POST['inputId'],
                                                        password=request.POST['inputPassword'],
                                                        name=request.POST['inputName'],
                                                        # phonenum=, // deleted fields
                                                        uid=request.POST['inputNumber']
                                                        )
            except ValueError:
                return JsonResponse({'message': 'Registration failed'})

## ID duplicate check        
def do_duplicate_check(request):
    if request.method == 'GET':
        usr_id = request.GET.get('inputId')
        try:
            _id = EngineerTB.objects.get(usr_id=usr_id)
            return JsonResponse({'duplicate': 'false'})
        except:
            return JsonResponse({'duplicate': 'true'})
        
def terms(request):
    return render(request, 'terms.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

