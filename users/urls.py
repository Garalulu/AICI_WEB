from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.login, name='login'),
    path('join', views.join, name='join'),
    path('terms', views.terms, name='terms'),
    path('terms_of_service', views.terms_of_service, name='terms_of_service'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]