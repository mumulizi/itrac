#!/usr/bin/env python
#_*_coding:utf-8_*_
#__author__="lihongxing"

from django.db import models
from problem import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta
# from itertools import chain

import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def my_page(request,days):
    '''
    WeekAndMonthPage()
    此功能是按照日期（一周以内或者一个月以内）合并查询的QuerySet然后做分页展示
    '''
    #定义一个空的QuerySet，用于过滤出来的QuerySet去合并
    lastNumDayAll = models.add_problem.objects.none()
    #获取当前时间
    currentTime= datetime.now()
    for i in range(days):
        num = i + 1
        #获取Num天以前的时间
        NumDay = currentTime + timedelta(days=-num)
        #格式化Num天以前的日期
        formatDate = NumDay.strftime("%Y-%m-%d")
        # print(formatDate)
        lastNumDay = 'lastNumDay'+str(i)
        #‘-id’根据id倒序查询过滤Num天以前的数据
        lastNumDay = models.add_problem.objects.filter(ProblemTime__contains = formatDate).order_by('-id')
        # print(lastNumDay)
        #合并QuerySet
        lastNumDayAll = lastNumDayAll | lastNumDay
    # print("----->all:",lastNumdayAll)
    if lastNumDayAll.count() == 0:
        return 0
    #分页，每页7条记录
    paginator = Paginator(lastNumDayAll,7)
    page = request.GET.get('page')
    try:
        lastNumDayAll_page = paginator.page(page)
    except PageNotAnInteger:
        lastNumDayAll_page = paginator.page(1)
    except EmptyPage:
        lastNumDayAll_page_page = paginator.page(paginator.num_pages)
    return lastNumDayAll_page