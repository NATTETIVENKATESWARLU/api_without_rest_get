"""
URL configuration for model_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("json",data_json),
    path("json1",data_jsoncbv.as_view()),
    path("json2/<int:id>/",data_jsoncbv1.as_view()),
    path("json3/<int:id>/",data_jsoncbv2.as_view()),
    path("json4/",data_jsoncbv3.as_view()),
    path("json5/",data_jsoncbv4.as_view()),
    path("json6/",data_jsoncbv5.as_view()),
    path("json7/<int:id>",data_jsoncbv6.as_view()),
    path("json8/<int:id>",data_jsoncbv7.as_view()),
]
