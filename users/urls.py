from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


app_name = 'users'
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('terms/join/', views.join, name='join'),
    path('terms/', views.terms, name='terms'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]