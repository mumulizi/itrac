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
    �˹����ǰ������ڣ�һ�����ڻ���һ�������ڣ��ϲ���ѯ��QuerySetȻ������ҳչʾ
    '''
    #����һ���յ�QuerySet�����ڹ��˳�����QuerySetȥ�ϲ�
    lastNumDayAll = models.add_problem.objects.none()
    #��ȡ��ǰʱ��
    currentTime= datetime.now()
    for i in range(days):
        num = i + 1
        #��ȡNum����ǰ��ʱ��
        NumDay = currentTime + timedelta(days=-num)
        #��ʽ��Num����ǰ������
        formatDate = NumDay.strftime("%Y-%m-%d")
        # print(formatDate)
        lastNumDay = 'lastNumDay'+str(i)
        #��-id������id�����ѯ����Num����ǰ������
        lastNumDay = models.add_problem.objects.filter(ProblemTime__contains = formatDate).order_by('-id')
        # print(lastNumDay)
        #�ϲ�QuerySet
        lastNumDayAll = lastNumDayAll | lastNumDay
    # print("----->all:",lastNumdayAll)
    if lastNumDayAll.count() == 0:
        return 0
    #��ҳ��ÿҳ7����¼
    paginator = Paginator(lastNumDayAll,7)
    page = request.GET.get('page')
    try:
        lastNumDayAll_page = paginator.page(page)
    except PageNotAnInteger:
        lastNumDayAll_page = paginator.page(1)
    except EmptyPage:
        lastNumDayAll_page_page = paginator.page(paginator.num_pages)
    return lastNumDayAll_page