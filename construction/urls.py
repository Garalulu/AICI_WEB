from django.urls import path
from . import views

app_name = 'construction'
urlpatterns = [
    path('', views.construction, name='construction'),
    path('upload/', views.upload_construction, name='construction_upload'),
]