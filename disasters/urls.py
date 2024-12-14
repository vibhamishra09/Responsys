from django.contrib.auth import admin
from django.urls import path,include
from disasters import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from disasters import *
urlpatterns = [
    path("", views.index,name= 'disasters'),
    path('about/',views.about,name="about"),

    ]