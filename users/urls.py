from django.urls import path

from . import views


app_name = 'users'  
urlpatterns = [
    path('login/', views.login_view, name='login'), # 로그인(첫 화면)
    path('logout/', views.logout_view, name='logout'), # logout
    
    path('terms/join/', views.join, name='join'), # 회원가입
    path('terms/join/do_duplicate_check/', views.do_duplicate_check),
    path('terms/', views.terms, name='terms'), # 회원가입 이용약관
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'), # 서비스 이용약관
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'), # 개인정보 처리방침
    path('aboutus/', views.aboutus, name='aboutus'), # About us
]