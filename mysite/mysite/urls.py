"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from notice.views import index, post_new, success_sending, no_log, register_request, login_request, logout_request
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

app_name = "notice"

urlpatterns = [
    path('admin', admin.site.urls, name="admin"),
    path('index', index, name='main'),
    path('', post_new, name="create"),
    path('register/', register_request, name="register"),
    path('notice/success', success_sending, name='successfully'),
    # path('login/', LoginView.as_view(template_name="notice/login.html"), name="login"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),
    path('nologin/', no_log, name='no log in'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


