#!/usr/bin/env python
#_*_coding:utf-8_*_
#__author__="lihongxing"


from django.conf.urls import url
from problem import  views
urlpatterns = [
    url(r'^$', views.index,name='problem_index'),
    url(r'^search', views.search,name='search'),
    url(r'^problem_list', views.search_list,name='problem_list'),
    url(r'^week', views.week,name='week'),
    url(r'^month', views.month,name='month'),
    url(r'^edit', views.edit,name='edit'),
]
