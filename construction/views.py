from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.datastructures import MultiValueDict
from django.utils import timezone
import magic

from users.decorators import login_required
from AICI_WEB.AI_mp3todb import construction
from .forms import ConstructionCallForm
from .models import ConstructionTB


@login_required
def construction(request):
    if request.method == 'GET':
        now = timezone.now()
        
        ## load constructions but only for engineer's work center
        _data = ConstructionTB.objects.filter(cent=request.user.uid.cent).order_by('receipt') 
        data = _data.filter(receipt__lte=now)
        return render(request, 'construction/construction.html', {'data': data})
    
    if request.method == 'POST':
        try:
            _data_post = MultiValueDict()
            _data_post['cstr_desc'] = request.POST['cstr_desc']
            _data_post['cstr_file'] = request.POST['cstr_file']
            current_user = request.POST['user_data']
            
            uploaded_file = request.FILES['cstr_file']
            file_content = uploaded_file.read(1024)
            mime_type = magic.from_buffer(file_content, mime=True)
            
            if mime_type == 'audio/mpeg' or mime_type == 'audio/x-m4a':
                form = ConstructionCallForm(_data_post, request.FILES)
                if form.is_valid():
                    _file = form.save()
                    
                    receipt, cstr_company, cstr_location = construction(request.FILES)
                    _call = ConstructionTB(receipt=receipt,
                                        cstr_company=cstr_company,
                                        cstr_location=cstr_location,
                                        cent=current_user,
                                        cstrcall=_file)
                    _call.save()
                    ## redirect to current page
                    return redirect('construction:construction')
        except KeyError:
            return JsonResponse({'message':'no file uploaded'})
        except Exception as e:
            return JsonResponse({'message': str(e)})
        
    return JsonResponse({'message': 'Upload failed'})