from django.shortcuts import render

from users.decorators import login_required
from board.models import BoardTB, UploadFile
from voc.models import CustomerTB

@login_required
def home(request):
    if request.method == 'GET':
        ## 공지사항 부분
        board = BoardTB.objects.all().order_by('-brd_id')
        ## voc부분
        df = CustomerTB.objects.all()
            
        return render(request, 'home.html', {'data': board,'df':df})
    