from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate

from .models import EngineerTB, UidTB
from .forms import CustomUserCreationForm


def login_view(request):
    if request.method == 'POST':
        usr_id = request.POST['usr_id']
        password = request.POST['password']
        user = authenticate(request, usr_id=usr_id, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login success'})
        else:
            return JsonResponse({'message': 'ID or password is incorrect'})
        
    if request.method == 'GET':
        ## Login status check
        if request.user.is_authenticated:
            return redirect('/') ## insta redirect to home if user is logined already
        else:
            return render(request, 'users/login.html')
            
def logout_view(request):
    logout(request)
    return redirect('users:login') ## redirect to login page

def join(request):
    ## Default page load
    if request.method == 'GET':
        return render(request, 'users/join.html')
    
    ## Signup request
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        ## Input check
        if form.is_valid():
            uid = request.POST['uid'].strip()
            uid_instance = UidTB.objects.filter(uid=uid) # Change uid to UidTB instance for matching with forein key correctly.
            
            ## Engineer duplicate check
            try:
                _user = EngineerTB.objects.get(uid=uid_instance)
            except Exception as e:
                _user = None          
            
            ## Success
            if _user is None:
                user = form.save()
                return JsonResponse({'message': 'Registration success'})
            
            ## Failed
            else:
                return JsonResponse({'message': 'Registration failed'})
        
        ## UID not match    
        else:
            return JsonResponse({'message': 'Invalid engineer id'})       
            
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


        

