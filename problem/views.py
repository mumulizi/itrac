#!/usr/bin/env python
#_*_coding:utf-8_*_

from django.shortcuts import render,HttpResponse,HttpResponseRedirect,render_to_response
from django.db import models
from problem import models
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils import WAMAPage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required

import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def login(request):
    if request.method == 'POST':
        #根据django自带的用户认证取出数据
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            #使用自带认证登录
            user_login(request,user)
            #登录成功返回首页
            username = request.POST.get('username')
            return HttpResponseRedirect('/problem/')
        else:
            #登录失败
            login_err = "Wrong username or password!"
            #返回错误消息
            return render(request, 'login.html', {'login_err':login_err})
    #如果是get
    return render(request, 'login.html')
#退出返回登录页
def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/problem/')



@login_required(login_url='/login/')
def index(request):
    if request.method =="POST":
        #获取前端提交过来的数据
        post_hostname = str(request.POST.get('hostname'))
        post_ipaddress = str(request.POST.get('ipaddress'))
        post_problem_user = str(request.POST.get('problem_user'))
        post_problem_time = str(request.POST.get('problem_time'))
        post_issue = str(request.POST.get('issue'))
        post_resolve = str(request.POST.get('resolve'))
        post_status = str(request.POST.get('status'))
        post_resolve_user = request.user.username
        # print(post_hostname,post_ipaddress,post_issue,post_problem_user,post_problem_time,post_resolve,post_status)

        #保存前端提交的数据到数据库
        save_post_data = models.add_problem(
            Hostname=post_hostname,IPaddress=post_ipaddress,ProblemUser=post_problem_user,
            ProblemTime=post_problem_time,Issue=post_issue, Resolve=post_resolve,
            ProblemStatus=post_status, ResolveUser=post_resolve_user
        )
        save_post_data.save()
    return  render(request, 'problem/index.html')

@login_required(login_url='/login/')
def search(request):
    return render(request,'problem/search.html')
@login_required(login_url='/login/')
def search_list(request):
    if request.method =="POST":
        post_search = request.POST.get('search','null')
        qset = (
            Q(Hostname__icontains = post_search) |
            Q(IPaddress__icontains = post_search) |
            Q(ProblemUser__icontains = post_search) |
            Q(ProblemTime__icontains = post_search) |
            Q(Issue__icontains = post_search)|
            Q(Resolve__icontains = post_search)|
            Q(ProblemStatus__icontains = post_search)|
            Q(ResolveUser__icontains = post_search)
            )

        #反转queryset 用于前端页面按照时间插入的倒序排序
        global problem_list_info
        problem_list_info = models.add_problem.objects.filter(qset).order_by('-id')
        if post_search =='' or problem_list_info.count() == 0:
            print(u"查询为空")
            # print("search + status:",post_search ,"+" ,problem_list)
            return render(request,'problem/search.html')
        #分页。每页展示N个
        paginator = Paginator(problem_list_info,7)
        page = request.GET.get('page')
        try:
            problem = paginator.page(page)
        except PageNotAnInteger:
            problem = paginator.page(1)
        except EmptyPage:
            problem = paginator.page(paginator.num_pages)
        return  render(request,'problem/problem_list.html',{'hostnames':problem})
    else:
        #django重启后用户未退出再刷新页面就不再是post返回的，而是get页面，此时proble_list_info就是未定义的了，所以需try一下
        try:
            paginator = Paginator(problem_list_info,7)
        except NameError:
            return render(request,'problem/search.html')
        page = request.GET.get('page')
        try:
            problem = paginator.page(page)
        except PageNotAnInteger:
            problem = paginator.page(1)
        except EmptyPage:
            problem = paginator.page(paginator.num_pages)
        return  render(request,'problem/problem_list.html',{'hostnames':problem})
@login_required(login_url='/login/')
def week(request):
    daysData = WAMAPage.my_page(request,7)
    if daysData == 0:
        return HttpResponse(u"根据时间日期未检索到最近一周未发生的故障记录，请重新选择或根据具体日期进行搜索")
    else:
        return render(request,'problem/week_list.html',{'hostnames':daysData})
@login_required(login_url='/login/')
def month(request):
    daysData = WAMAPage.my_page(request,30)
    if daysData == 0:
        return HttpResponse(u"根据时间日期未检索到最近一个月未发生的故障记录，请重新选择或根据具体日期进行搜索")
    else:
        return render(request,'problem/month_list.html',{'hostnames':daysData})


def edit(request):
    if request.method=="POST":
        post_id = int(request.POST.get('id'))
        post_hostname = str(request.POST.get('hostname'))
        post_ipaddress = str(request.POST.get('ipaddress'))
        post_problem_user = str(request.POST.get('problem_user'))
        post_problem_time = str(request.POST.get('problem_time'))
        post_issue = str(request.POST.get('issue'))
        post_resolve = str(request.POST.get('resolve'))
        post_status = str(request.POST.get('status'))
        post_resolve_user = request.user.username

        models.add_problem.objects.filter(id=post_id).update(Hostname=post_hostname,IPaddress=post_ipaddress,ProblemUser=post_problem_user,
            ProblemTime=post_problem_time,Issue=post_issue, Resolve=post_resolve,
            ProblemStatus=post_status, ResolveUser=post_resolve_user)
        print(post_id,post_hostname,post_ipaddress,post_status)
        return HttpResponse("编辑保存成功")







def week_bak_file_not_use_del(request):
    #定义一个空的QuerySet，用于过滤出来的QuerySet去合并
    lastWeekAll = models.add_problem.objects.none()
    #获取当前时间
    currentTime= datetime.now()
    for i in range(7):
        num = i + 1
        #获取七天以前的时间
        sevenDay = currentTime + timedelta(days=-num)
        #格式化七天以前的日期
        formatDate = sevenDay.strftime("%Y-%m-%d")
        print(formatDate)
        lastWeek = 'lastWeek'+str(i)
        #查询过滤七天以前的数据
        lastWeek = models.add_problem.objects.filter(ProblemTime__contains = formatDate).order_by('-id')
        # print(lastWeek)
        #合并QuerySet
        lastWeekAll = lastWeekAll | lastWeek
    # print("----->all:",lastWeekAll)
    if lastWeekAll.count() == 0:
        return HttpResponse(u"根据时间日期未检索到最近一周未发生的故障记录，请重新选择或根据具体日期进行搜索")
    #分页，每页7条记录
    paginator = Paginator(lastWeekAll,7)
    page = request.GET.get('page')
    try:
        lastWeekAll_page = paginator.page(page)
    except PageNotAnInteger:
        lastWeekAll_page = paginator.page(1)
    except EmptyPage:
        lastWeekAll_page = paginator.page(paginator.num_pages)
    return render(request,'problem/week_list.html',{'hostnames':lastWeekAll_page})