from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login
import json

from .models import EngineerTB, UidTB
from .forms import CustomUserCreationForm


# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def join(request):
    ## Default page load
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'users/join.html', {'form': form})
    
    ## Signup request
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
            else:
                return JsonResponse({'message': 'Login failed'})
                
        '''if request.POST.get('inputPassword') == request.POST.get('inputPasswordCk'):
            uid = request.POST.get('inputNumber').strip()
            uid_instance = UidTB.objects.filter(uid=uid) # Change uid to UidTB instance for matching with forein key correctly.
            if uid_instance:
                ## Name match check
                if EngineerTB.objects.filter(name=uid_instance[0].name):
                    new_user = EngineerTB.objects.create_user(usr_id=request.POST.get('inputId'),
                                                            password=request.POST.get('inputPassword'),
                                                            name=request.POST.get('inputName'),
                                                            ## phonenum=, // deleted fields
                                                            uid=uid_instance
                                                            )
                    return JsonResponse({'message': 'Registration success'})
                else:
                    return JsonResponse({'message': 'engineer name does not match'})
            else:
                return JsonResponse({'message': "Invalid engineer id"})
        return JsonResponse({'message': 'Registration failed'})'''
            
            

## ID duplicate check        
def do_duplicate_check(request):
    if request.method == 'GET':
        usr_id = request.GET['usr_id']
        try:
            _id = EngineerTB.objects.get(usr_id=usr_id)
        except Exception as e:
            _id = None
        return JsonResponse({'duplicate': usr_id if _id is None else 'true'})
            
        
def terms(request):
    return render(request, 'users/terms.html')

def terms_of_service(request):
    return render(request, 'users/terms_of_service.html')

def privacy_policy(request):
    return render(request, 'users/privacy_policy.html')

def home(request):
    return render(request, 'users/home.html')

