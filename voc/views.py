from django.shortcuts import render

# Create your views here.

def tmcheck(request):
    return render(request, 'voc/tmcheck.html')