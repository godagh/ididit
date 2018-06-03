'''
Created on 2018. 6. 2.

@author: 1104-2
'''
from django.urls import path 
from .views import *
app_name = 'blog'
urlpatterns = [
    path('',index,name='index'),
    path('<int:post_id>/',detail,name='detail'),
    path('posting/',posting,name='posting'),
    ]