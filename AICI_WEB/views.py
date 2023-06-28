from django.shortcuts import render

from users.decorators import login_required
from board.models import BoardTB, UploadFile

@login_required
def home(request):
    if request.method == 'GET':
        board = BoardTB.objects.all().order_by('-brd_id')
        data = []
        for i in range(3):
            board_data = {
                'brd_id': board[i].brd_id,
                'brd_title': board[i].brd_title,
                'brd_create': board[i].brd_create.strftime('%Y-%m-%d %H:%M:%S') if board[i].brd_create else None,
            }
            data.append(board_data)
            
        return render(request, 'home.html', {'data': data})
