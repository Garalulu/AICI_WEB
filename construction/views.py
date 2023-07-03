import magic

from django.http import JsonResponse
from django.shortcuts import render, redirect

from users.decorators import login_required

from AICI_WEB.AI_mp3todb import construction

from .models import ConstructionTB
from .forms import ConstructionCallForm


@login_required
def construction_list(request):
    data = ConstructionTB.objects.filter(cstrcall__cent=request.user.uid.cent).order_by(
        "receipt"
    )
    return render(request, "construction/construction.html", {"data": data})


@login_required
def construction_upload(request):
    if request.method == "POST":
        try:
            uploaded_file = request.FILES["cstr_file"]
            file_content = uploaded_file.read(1024)
            mime_type = magic.from_buffer(file_content, mime=True)

            if mime_type == "audio/mpeg" or mime_type == "audio/x-m4a":
                form = ConstructionCallForm(request.POST, request.FILES)
                if form.is_valid():
                    receipt, cstr_company, cstr_location = construction(
                        request.FILES["cstr_file"]
                    )
                    _file = form.save()
                    _call = ConstructionTB(
                        receipt=receipt,
                        cstr_company=cstr_company,
                        cstr_location=cstr_location,
                        ##cstr_company=.
                        ##cstr_manager=.
                        cstrcall=_file,
                    )
                    _call.save()
                    # Redirect to current page
                    return redirect("construction:construction")
            else:
                # Form is not valid
                print(form.errors)
                return JsonResponse({"message": "Invalid form data"})
        except Exception as e:
            return JsonResponse({"message": str(e)})

    return JsonResponse({"message": "Upload failed"})
