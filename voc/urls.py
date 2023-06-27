from django.urls import path
from voc import views

app_name = 'voc'
urlpatterns = [
    path('', views.tmcheck, name='tmcheck'),
    path('upload/', views.upload_voc, name='voc_upload'),
    path('customer_list/', views.customer_list, name='customer_list'),
]