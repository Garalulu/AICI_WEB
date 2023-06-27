from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.notice, name='notice'),
    path('post/', views.post, name='post'),
    path('content/', views.content, name='content'),
]