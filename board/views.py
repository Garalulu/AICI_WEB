from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BoardForm, UploadFileForm
from .models import BoardTB, UploadFile
from users.models import EngineerTB

def notice(request):
    data = BoardTB.objects.all().order_by('-brd_id')
    return render(request, 'board/notice.html', {'data': data})

def post(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        file_form = UploadFileForm(request.POST, request.FILES)
        print(file_form.errors)
        if board_form.is_valid():
            board = board_form.save(commit=False)
            board.usr_id = EngineerTB.objects.get(id=request.user.id)
            board.save()

            if file_form.is_valid():
                file = request.FILES.get('file')
                if file:
                    upload_file = UploadFile(brd_id=board, file=file)
                    upload_file.save()
                else:
                # 파일이 선택되지 않은 경우에 대한 처리
                    upload_file = UploadFile(brd_id=board)
                    upload_file.save()

            response_data = {'message': '게시물이 성공적으로 생성되었습니다.'}
            return JsonResponse(response_data)

        else:
            response_data = {'message': '게시글을 게시하는데 실패하였습니다.'}
            return JsonResponse(response_data, status=400)

    else:
        board_form = BoardForm()
        file_form = UploadFileForm()
        return render(request, 'board/post.html', {'board_form': board_form, 'file_form': file_form})





def content(request, brd_id):
    data = BoardTB.objects.all()
    for board in data:
        if board.brd_id == brd_id:
            data = board
            
    return render(request, 'board/content.html', {'data': data})

def board_list(request):
    if request.method == 'GET':
        boards = BoardTB.objects.all()
        boards = BoardTB.objects.order_by('-brd_id')  # brd_id 내림차순 정렬
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
   
