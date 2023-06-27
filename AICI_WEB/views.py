from django.shortcuts import render

from users.decorators import login_required


@login_required
def home(request):
    if request.method == 'GET':
        return render(request, 'users/home.html')