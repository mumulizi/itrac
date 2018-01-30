#!/usr/bin/env python
#_*_coding:utf-8_*_
from django.contrib import admin

# Register your models here.
from problem import models


admin.site.register(models.add_problem)