"""edu4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main.views import home, appl_info, success_appln, scholarships, categories, engineering, medical, humanities, management
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import registerpage, loginpage, logoutUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('scholarships/', scholarships, name = 'scholarships'),
    path('ctgs/', categories, name = 'ctgs'),
    path('engineering/', engineering, name = 'engineering'),
    path('medical/', medical, name = 'medical'),
    path('humanities/', humanities, name = 'humanities'),
    path('management', management, name = 'mang'),
    path('register/', registerpage, name = 'register'),
    path('login/', loginpage, name = 'login1'),
    path('logout/', logoutUser, name = 'logout1'),
    path('application/', appl_info, name='appln_info'),
    path('successfull/', success_appln, name='success_appln'),
    path('accounts/', include('django.contrib.auth.urls')),
]