from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import BoardTB
from .forms import BoardForm
# Create your views here.

def notice(request):
    return render(request, 'board/notice.html')

def post(request):
    return render(request, 'board/post.html')

def content(request):
    return render(request, 'board/content.html')

def board_list(request):
    if request.method == 'GET':
        boards = BoardTB.objects.all()
        data = []

        for board in boards:
            board_data = {
                'usr_id': board.usr_id.id,
                'brd_title': board.brd_title,
                'brd_content': board.brd_content,
                'brd_create': board.brd_create.strftime('%Y-%m-%d %H:%M:%S'),
                'brd_update': board.brd_update.strftime('%Y-%m-%d %H:%M:%S')
            }
            data.append(board_data)

        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': '게시물이 성공적으로 생성되었습니다.'})
        else:
            return JsonResponse({'message': '유효하지 않은 데이터입니다.'}, status=400)
