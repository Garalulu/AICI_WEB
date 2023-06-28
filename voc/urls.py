from django.urls import path
from voc import views

app_name = 'voc'
urlpatterns = [
    path('', views.tmcheck, name='tmcheck'),
]