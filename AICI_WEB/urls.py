"""
URL configuration for AICI_WEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),  ## admin site
    path("", home, name="home"),  # 메인 홈
    path("users/", include("users.urls")),  # 로그인, 회원가입, 약관
    path("board/", include("board.urls"), name="board"),  # 게시판
    path("voc/", include("voc.urls")),  # VOC
    path("construction/", include("construction.urls")),  # 시외공사
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
