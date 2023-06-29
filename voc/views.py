from django.shortcuts import render, redirect
from django.http import JsonResponse
import magic

from users.decorators import login_required
from AICI_WEB.AI_mp3todb import voc
from .exceltodb import exceltodb
from .forms import VOCForm
from .models import CustomerTB

## tmcheck
## get voc main page with voc data from dbCustomerTB
@login_required
def tmcheck(request):
    if request.method == 'GET':
        ## load voc but only for engineer's work center
        data = CustomerTB.objects.filter(cent=request.user.uid.cent).order_by('receipt')
        form = VOCForm()
        return render(request, 'voc/tmcheck.html', {'data': data,
                                                    'form': form,})
    ## get excel file and extract data to db    
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['voc_file']
            file_content = uploaded_file.read(1024)
            mime_type = magic.from_buffer(file_content, mime=True)
            # return JsonResponse({"message":mime_type})
            if mime_type == 'application/zip':
                form = VOCForm(request.POST, request.FILES)
                if form.is_valid():
                    _file = form.save()
                    exceltodb(_file) ## extract data in VOCTB to CustomerTB
                    return redirect('/')
                else:
                    return JsonResponse({'message': 'Invalid form data'})
<<<<<<< HEAD
            elif mime_type == 'audio/mpeg' or mime_type == 'audio/x-m4a':
                _data = CustomerTB.objects.last()
                tm_judge, tm_result, cust_importance = voc(request.FILES['voc_file'])
                _data.tm_judge = tm_judge
                _data.tm_result = tm_result
                _data.cust_importance = cust_importance
                _data.save()
                return redirect('/')
            else:
                ## if the file is not .xls, .mp3
                return JsonResponse({'message': 'Invalid file type'})
                
        except KeyError:
            return JsonResponse({'message':'no file uploaded'})
        except Exception as e:
            return JsonResponse({'message': str(e)})
            
=======
            elif mime_type == 'audio/mpeg':
                _data = CustomerTB.objects.get()
                _data.tm_judge, _data.tm_result, _data.cust_importance = voc(request.FILES)
                _data.save()
                return redirect('/')
        except:
            ## if the file is not .xls, .mp3
            return JsonResponse({'message': 'Invalid file type'})
>>>>>>> cc6cb02e501231a98a4c1383f3d4f058b954a3fa
    
'''def voc(request):
    data = CustomerTB.objects.all()
    return render(request, 'voc/tmcheck.html', {'data':data})'''