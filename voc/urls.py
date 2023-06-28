from django.urls import path
from voc import views

app_name = 'voc'
urlpatterns = [
    path('', views.tmcheck, name='tmcheck'),
    # path('upload/', views.upload_voc, name='voc_upload'),
    path('upload_voc/', views.upload_voc, name='upload_voc'),
    # path('excelupload', views.ExcelUploadView.as_view(), name='excel-upload'),
]