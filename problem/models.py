#!/usr/bin/env python
#_*_coding:utf-8_*_
from __future__ import unicode_literals
from django.db import models

class add_problem(models.Model):
    Hostname = models.CharField(max_length=125)
    IPaddress = models.GenericIPAddressField()
    ProblemUser = models.CharField(max_length=30)
    ProblemTime = models.CharField(max_length=40,verbose_name=u"报修时间")
    Issue = models.TextField(verbose_name=u"问题")
    Resolve = models.TextField(verbose_name=u"解决方法",blank=True,null=True)
    ProblemChoice = (
        ('yes',u'以解决'),
        ('no',u'未解决'),
        ('wait',u'待解决')
    )
    ProblemStatus = models.CharField(max_length=10,choices=ProblemChoice,default='no',verbose_name=u"是否完成")
    ResolveUser = models.CharField(max_length=20,verbose_name=u'处理人')
    def __str__(self):
        return self.Hostname

