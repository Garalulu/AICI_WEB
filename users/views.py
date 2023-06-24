from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def join(request):
    return render(request, 'join.html')

def terms(request):
    return render(request, 'terms.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

