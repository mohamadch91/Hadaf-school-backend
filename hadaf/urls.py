"""hadaf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('slider/',include('slider.urls')),
    path('quiz/',include('quiz.urls')),
    # path('forum/',include('forum.urls')),
    path('course/',include('course.urls')),
    path('archive/',include('archive.urls')),
    path('authen/',include('authen.urls')),
    path('courseDEP/',include('courseDEP.urls')),
    path('discount/',include('discount.urls')),
    path('sms/',include('sms.urls')),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
