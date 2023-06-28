from django.shortcuts import render

from users.decorators import login_required
from board.models import BoardTB, UploadFile
from voc.models import CustomerTB

@login_required
def home(request):
    if request.method == 'GET':
        ## 공지사항 부분
        board = BoardTB.objects.all().order_by('-brd_id')
        data = []
        for i in range(3):
            board_data = {
                'brd_id': board[i].brd_id,
                'brd_title': board[i].brd_title,
                'usr_name': board[i].usr_id.name,
                'brd_create': board[i].brd_create.strftime('%Y-%m-%d %H:%M:%S') if board[i].brd_create else None,
            }
            data.append(board_data)
        ## voc부분
        df = CustomerTB.objects.all()
            
        return render(request, 'home.html', {'data': data,'df':df})
    