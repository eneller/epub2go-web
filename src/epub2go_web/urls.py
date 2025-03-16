"""
URL configuration for epub2go_web project.

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
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

def root(request:HttpRequest):
    title = 'epub2go'
    targetParam = request.GET.get('t', None)
    if targetParam is not None:
        getEpub(targetParam)
    return render(request, 'index.html', locals())

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',root, name='root')
]

def getEpub(param):
    # TODO validate / sanitize input
    # TODO check for existing file and age
    # TODO download
    # TODO redirect to loading page
    # TODO redirect to download page
    raise NotImplementedError
