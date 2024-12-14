"""
URL configuration for disaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import admin
from django.urls import path,include
from disasters import *
from disasters import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
urlpatterns = [
   
    path('',include('disasters.urls')),
    path("about",views.about,name='about'),
    path('services/<int:id>/',views.services,name='services'),
    path("services<id>",views.services,name='services'),
    path("services//",views.services,name='services'),
    path('delete/<id>/', views.delete , name="delete"),
    path("login/",views.login_page,name='login_page'),
    path("login",views.login_page,name='login_page'),
    path('index/',views.index,name='index'),
      path('register/',views.register,name='register'),
       
]
