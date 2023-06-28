from django.shortcuts import render
from django.http import JsonResponse

from users.decorators import login_required
from .exceltodb import exceltodb
from .forms import VOCForm

@login_required
def tmcheck(request):
    if request.method == 'GET':
        form = VOCForm()
        return render(request, 'voc/tmcheck.html', {'form': form})
    if request.method == 'POST':
        form = VOCForm(request.POST, request.FILES)
        if form.is_valid():
            _file = form.save()
            exceltodb(_file) ## extract data in VOCTB to CustomerTB
            return JsonResponse({'message': 'Upload success'})
        else:
            return JsonResponse({'message': 'Invalid form data'})
    return JsonResponse({'message': 'Upload failed'})
    
    
@login_required
def upload_voc(request):
    if request.method == 'POST' and request.FILES['cstr_file']:
        form = VOCForm(request.POST, request.FILES)
        if form.is_valid():
            _file = form.save()
            exceltodb(_file) ## extract data in VOCTB to CustomerTB
            return JsonResponse({'message': 'Upload success'})
        else:
            return JsonResponse({'message': 'Invalid form data'})
    return JsonResponse({'message': 'Upload failed'})

# class ExcelUploadView(View):
#     def post(self, request):
#         excelFile = request.FILES['file']
        
#         excel = openpyxl.load_workbook(excelFile, data_only=True)
#         work_sheet = excel.worksheets[0]
        
#         all_values = []
#         for row in work_sheet.rows:
#             row_value = []
#             for cell in row:
#                 row_value.append(cell.value)
#             all_values.append(row_value)
            
#         for row in all_values:
#             sample_model = SampleModel(Number=row[0], Name=row[1], Item=row[2])
#             sample_model.save()
            
#         response = {'status':1, 'message': '엑셀파일이 업로드 됐습니다.'}
#         return GttpResponse(json.dumps(response), content_type='application/json')
