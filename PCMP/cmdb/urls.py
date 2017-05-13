from django.conf.urls import url, include
from django.contrib import admin
from cmdb import views

urlpatterns = [
#    url(r'^test/', views.test),
    url(r'^receive_server_info/', views.receive_server_info),
    url(r'^CreateServer/', views.create_server),
    url(r'^ManageServer/', views.manage_server),
    url(r'^ListConfig/', views.list_config),

]
