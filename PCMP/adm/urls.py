from django.conf.urls import url, include
from django.contrib import admin
from adm import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^login1/$', views.login1),
    url(r'^index/', views.index),
    url(r'^register/', views.register),

]
