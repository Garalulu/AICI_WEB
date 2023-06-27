from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import BoardTB
from .forms import BoardForm

def notice(request):
    return render(request, 'board/notice.html')

def post(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            response_data = {'message': '게시물이 성공적으로 생성되었습니다.'}
            return JsonResponse(response_data)
        else:
            response_data = {'message': '유효하지 않은 데이터입니다.'}
            return JsonResponse(response_data, status=400)
    else:
        form = BoardForm()
        return render(request, 'board/post.html', {'form': form})

def content(request):
    return render(request, 'board/content.html')

def board_list(request):
    if request.method == 'GET':
        boards = BoardTB.objects.all()
        data = []

        for board in boards:
            board_data = {
                'brd_id': board.brd_id,
                'brd_title': board.brd_title,
                'brd_content': board.brd_content,
                'brd_create': board.brd_create.strftime('%Y-%m-%d %H:%M:%S') if board.brd_create else None,
                'brd_update': board.brd_update.strftime('%Y-%m-%d %H:%M:%S') if board.brd_create else None,
            }
            data.append(board_data)

        return JsonResponse(data, safe=False)
