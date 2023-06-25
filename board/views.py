from django.shortcuts import render

# Create your views here.

def notice(request):
    return render(request, 'board/notice.html')

def post(request):
    return render(request, 'board/post.html')

def content(request):
    return render(request, 'board/content.html')