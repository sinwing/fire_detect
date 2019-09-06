"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from yolo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main),
    path('stream_yolo_start',views.stream_yolo_start),
    path('yolosite',views.yolosite),
    path('video_yolo_start1',views.video_yolo_start1),
    path('video_yolo_start2',views.video_yolo_start2),
    path('label_list_get',views.label_list_get),
    path('lf_accumulate',views.lf_accumulate),
    path('videofile1',views.videofile1),
    path('videofile2',views.videofile2),
    path('seoul_fireoffice_weather_info',views.seoul_fireoffice_weather_info),
    path('incheon_fireoffice_weather_info',views.incheon_fireoffice_weather_info),
    path('gwangju_fireoffice_weather_info',views.gwangju_fireoffice_weather_info),
    path('mail',views.mail),
]
