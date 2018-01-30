#!/usr/bin/env python
#_*_coding:utf-8_*_
from django.conf.urls import url,include
from django.contrib import admin
from problem import  url as pro_url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^problem/',include(pro_url))
]
