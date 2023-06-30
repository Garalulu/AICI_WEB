from django.urls import path
from . import views

app_name = 'construction'

urlpatterns = [
    path('', views.construction_list, name='construction'),
    path('upload/', views.construction_upload, name='construction_upload'),
]
