from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BoardForm, UploadFileForm
from .models import BoardTB, UploadFile
from users.models import EngineerTB

def notice(request):
    return render(request, 'board/notice.html')

def post(request):
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        file_form = UploadFileForm(request.POST, request.FILES)

        if board_form.is_valid():
            board = board_form.save(commit=False)
            board_form.instance.usr_id = EngineerTB.objects.get(id=request.user.id)  # 현재 로그인한 사용자의 EngineerTB 인스턴스를 가져와 usr_id에 할당
            board.save()

            if file_form.is_valid() or not request.FILES:
                files = request.FILES.getlist('file')
                for file in files:
                    upload_file = UploadFile(file=file)
                    upload_file.save()
                    board.uploadfile_set.add(upload_file)  # 게시물과 파일 연결

            response_data = {'message': '게시물이 성공적으로 생성되었습니다.'}
            return JsonResponse(response_data)

        else:
            response_data = {'message': '게시글을 게시하는데 실패하였습니다.'}
            print('board_form 오류:', board_form.errors)
            print('file_form 오류:', file_form.errors)
            return JsonResponse(response_data, status=400)

    else:
        board_form = BoardForm()
        file_form = UploadFileForm()
        return render(request, 'board/post.html', {'board_form': board_form, 'file_form': file_form})




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
